from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='partitionpi',
    version='0.0.2',
    url='https://github.com/luansimoes/partitionpi',
    license='MIT License',
    author='Luan Simões',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='luansimoes@cos.ufrj.br',
    keywords='integer-partition texture music partitional analysis',
    description='Python library to handle integer partitions and compute partitional analysis metrics.',
    packages=find_packages(include=['partitionpi', 'partitionpi.*']),
    install_requires=['networkx>=3','matplotlib>=3'],)