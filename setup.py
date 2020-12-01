from setuptools import setup, find_packages

setup(
    name='Jarbas',
    version='1.0.0',
    author='Ricardo Maia',
    author_email='ricardo.ja.maia@gmail.com',
    description='Python Machine learning app',
    packages=find_packages(),
    install_requires=['tensorflow >= 2.3.1', 'opencv-python >= 4.4.0.46', 'numpy >= 1.18.5', 'matplotlib >= 1.5.1'],
)