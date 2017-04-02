from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='ezvm',
    version='0.0.0',
    description='',
    author='minggrim',
    install_requires=requirements,
    packages=find_packages(),
    data_files=[
        ('/usr/bin', ['pyezvm'])
    ]
)
