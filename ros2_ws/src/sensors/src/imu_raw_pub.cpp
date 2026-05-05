#include <chrono>
#include <memory>
#include <fcntl.h>
#include <linux/i2c-dev.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <cstdint>
#include <stdexcept>
#include <cmath>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float32_multi_array.hpp"

using namespace std::chrono_literals;

// IMU Driver
const char* I2C_DEVICE  = "/dev/i2c-7";
const int   IMU_ADDR    = 0x6A;

const uint8_t WHO_AM_I  = 0x0F;
const uint8_t CTRL1_XL  = 0x10;
const uint8_t CTRL2_G   = 0x11;
const uint8_t CTRL3_C   = 0x12;
const uint8_t OUTX_L_G  = 0x22;
const uint8_t OUTX_L_XL = 0x28;

constexpr double ACCEL_SCALE = 0.061e-3 * 9.80665; // ±2g  → m/s²
constexpr double GYRO_SCALE  = 8.75e-3 * (M_PI / 180.0); // ±250 dps → rad/s

class ISM330DLC {
public:
    ISM330DLC() {
        if ((fd = open(I2C_DEVICE, O_RDWR)) < 0)
            throw std::runtime_error("Failed to open I2C bus");
        if (ioctl(fd, I2C_SLAVE, IMU_ADDR) < 0)
            throw std::runtime_error("Failed to set I2C slave address");

        uint8_t id = read_reg(WHO_AM_I);
        if (id != 0x6B)
            throw std::runtime_error("WHO_AM_I mismatch");

        uint8_t ctrl3 = read_reg(CTRL3_C);
        write_reg(CTRL3_C, ctrl3 | 0x44);
        write_reg(CTRL1_XL, 0x40);  // 104 Hz, ±2g
        write_reg(CTRL2_G,  0x40);  // 104 Hz, ±250 dps
        usleep(100000);
    }

    ~ISM330DLC() { if (fd >= 0) close(fd); }

    void read_raw(uint8_t start_reg, int16_t out[3]) {
        uint8_t data[6];
        if (write(fd, &start_reg, 1) != 1) return;
        if (read(fd, data, 6) != 6) return;
        out[0] = (int16_t)(data[0] | (data[1] << 8));
        out[1] = (int16_t)(data[2] | (data[3] << 8));
        out[2] = (int16_t)(data[4] | (data[5] << 8));
    }

private:
    int fd;

    void write_reg(uint8_t reg, uint8_t value) {
        uint8_t buf[2] = {reg, value};
        if (write(fd, buf, 2) != 2)
            throw std::runtime_error("Failed to write I2C register");
    }

    uint8_t read_reg(uint8_t reg) {
        if (write(fd, &reg, 1) != 1)
            throw std::runtime_error("Failed to set register pointer");
        uint8_t value;
        if (read(fd, &value, 1) != 1)
            throw std::runtime_error("Failed to read register");
        return value;
    }
};

//ROS 2 Node 

class ImuPublisher : public rclcpp::Node
{
public:
    ImuPublisher()
    : Node("imu_publisher"), imu_()
    {
        // Publishes [accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z]
        publisher_ = this->create_publisher<std_msgs::msg::Float32MultiArray>("imu/data", 10);

        timer_ = this->create_wall_timer(
            50ms,
            std::bind(&ImuPublisher::timer_callback, this));

        RCLCPP_INFO(this->get_logger(), "IMU Publisher started");
        RCLCPP_INFO(this->get_logger(), "Test");
        RCLCPP_INFO(this->get_logger(), "Topic: imu/data  [ax, ay, az (m/s²), gx, gy, gz (rad/s)]");
    }

private:
    void timer_callback()
    {
        int16_t accel[3], gyro[3];
        imu_.read_raw(OUTX_L_XL, accel);
        imu_.read_raw(OUTX_L_G,  gyro);

        auto msg = std_msgs::msg::Float32MultiArray();

        // Layout description (optional but helpful for subscribers)
        msg.layout.dim.resize(1);
        msg.layout.dim[0].label  = "imu_data";
        msg.layout.dim[0].size   = 6;
        msg.layout.dim[0].stride = 6;

        // [0] accel_x  [1] accel_y  [2] accel_z  (m/s²)
        // [3] gyro_x   [4] gyro_y   [5] gyro_z   (rad/s)
        msg.data = {
            static_cast<float>(accel[0] * ACCEL_SCALE),
            static_cast<float>(accel[1] * ACCEL_SCALE),
            static_cast<float>(accel[2] * ACCEL_SCALE),
            static_cast<float>(gyro[0]  * GYRO_SCALE),
            static_cast<float>(gyro[1]  * GYRO_SCALE),
            static_cast<float>(gyro[2]  * GYRO_SCALE)
        };

        publisher_->publish(msg);
    }

    ISM330DLC imu_;
    rclcpp::Publisher<std_msgs::msg::Float32MultiArray>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};



int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<ImuPublisher>());
    rclcpp::shutdown();
    return 0;
}