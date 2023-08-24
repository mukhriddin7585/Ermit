from setuptools import setup

setup(
    name='Ermit',
    version='0.1.0',
    description='Ermit spline',
    author='Mukhriddin Abduganiev',
    author_email="mr.muhriddin.20@gmail.com",
    url="https://github.com/mukhriddin7585/Ermit",
    license='MIT',
    python_requires='>3.11.4',
    packages=['ermit'],
    install_requires=[
        'matplotlib==3.8.0rc1',
        'numpy==1.25.2'
    ],
    setup_requires=['pytest-runner==6.0.0'],
    tests_require=['pytest==7.4.0'],
    test_suite='tests',
)
