from setuptools import find_packages, setup

setup(
    name='gym_go',
    version='0.0.1',
    install_requires=['gym'],  # and other dependencies
    packages=find_packages(),
)
