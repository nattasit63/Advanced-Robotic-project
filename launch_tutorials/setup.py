from setuptools import setup
from glob import glob
import os
package_name = 'launch_tutorials'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name),glob('launch/launch_tutorials.launch.py')),

    
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='imchin',
    maintainer_email='imarkchin@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'killservice_node = launch_tutorials.killservice_node:main',
            'viapointservice_node = launch_tutorials.viapoint_service:main',
        ],
    },
)
