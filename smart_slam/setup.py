import os
from glob import glob, iglob
from setuptools import find_packages, setup

package_name = 'smart_slam'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Dhruv Chanana',
    maintainer_email='dchanana@purdue.edu',
    description='CS592 Smart SLAM project',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera = smart_slam.camera:main'
        ],
    },
)
