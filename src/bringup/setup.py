from setuptools import find_packages, setup
import os

package_name = 'bringup'

launch_files = [os.path.join('launch', file) for file in os.listdir('launch') if file.endswith('.py')]
config_files = [os.path.join('config', file) for file in os.listdir('config')]

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name +'/launch', launch_files),
        ('share/' + package_name +'/config', config_files),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='simon',
    maintainer_email='simon@gmail.com.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
