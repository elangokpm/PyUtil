from setuptools import setup, find_packages

setup(
    name = 'PyUtil',
    version = '1.0.0',
    url = 'https://github.com/mypackage.git',
    author = 'Elango K',
    description = 'python utilities for machine learning',
    packages = find_packages(),    
    install_requires = ['numpy >= 1.11.1', 'pandas >= 0.23.0', 'seaborn >= 0.8.1'],
)
