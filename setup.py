from setuptools import setup
import os
from glob import glob

package_name = 'restaurant_world'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.py')),
        ('share/' + package_name + '/worlds', glob('worlds/*.world')),
        ('share/' + package_name + '/maps', glob('maps/*')),
        ('share/' + package_name + '/scripts', glob('scripts/*.py')),  # Include your script
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='surya',
    maintainer_email='surya@todo.todo',
    description='A restaurant simulation world for TurtleBot3 in Gazebo',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'multi_point_nav = restaurant_world.scripts.multi_point_nav:main',
        ],
    },
)

