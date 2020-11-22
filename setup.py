from setuptools import setup, find_packages

import app

setup(
    name='app',
    version=app.__version__,
    author='Ricardo Maia',
    author_email='ricardo.ja.maia@gmail.com',
    description='Python Machine learning app',
    packages=find_packages(),
    install_requires=['tensorflow >= 2.3.1', 'opencv-python >= 4.4.0.46', 'numpy >= 1.18.5', 'matplotlib >= 1.5.1'], # Specify you app dependencies here
)