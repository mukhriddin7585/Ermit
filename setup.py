from setuptools import find_packages, setup

setup(
    name='Ermit',
    packages=find_packages(include=['ermit']),
    version='0.1.0',
    description='Ermit splayn',
    author='Mukhriddin Abduganiev',
    license='MIT',
    install_requires=['matplotlib==3.8.0rc1', 'numpy==1.25.2'],
    setup_requires=['pytest-runner==6.0.0'],
    tests_require=['pytest==7.4.0'],
    test_suite='tests',
)
