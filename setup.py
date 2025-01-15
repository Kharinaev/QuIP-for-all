from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='quipsharp',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    author='Your Name',
    author_email='your.email@example.com',
    description='QuIP-for-all',
    url='https://github.com/your-repo-url',
)