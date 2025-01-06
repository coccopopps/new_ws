from setuptools import find_packages, setup

package_name = 'wheelchair_simv2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/urdf', ['urdf/wheelchair.xacro']),
        ('share/' + package_name + '/launch', ['launch/display.launch.py']),
        # Add more directories if you have other files (e.g., meshes)
        # Example: ('share/' + package_name + '/meshes', ['meshes/example.stl'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pops',
    maintainer_email='pops@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
