from setuptools import setup

package_name = 'drive'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lunabotics',
    maintainer_email='lunabotics@todo.todo',
    description='Tank drive with RoboClaw',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'tank_drive = drive.tank_drive:main',   
            'pico_drive = drive.pico_drive:main',
            'auto_drive = drive.auto_drive:main',
            'auto_pub_test = drive.auto_pub_test:main',
        ],
    },
)