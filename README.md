# Machine Learning Python Container
This project provides the basis for starting a machine learning project using Remote-Containers in MS Visual Source Code.
Several machine learning related packages are installed by default:
- [Numpy][1]: a porwerfull and well known general-purpose array-processing and scientic computing package.
- [Matplotlib][2]: a comprehensive library for creating static, animated, and interactive visualizations in Python.
- [Tensorflow 2][3]: an open source machine learning framework developed by Google Brain.
- [Scikit-learn][4]: an open source machine learning framework.
- [Pytorch][5]: an open source machine learning framework.
- [Pandas][6]: a fast, powerful, flexible and easy to use open source data analysis and manipulation tool.

The base container relies on mcr.microsoft.com/vscode/devcontainers/python

## Benefits
Easily start a Python machine learning project without the hassle of configuring a development environment. This containers provides:
- Application source and test directories and initial files
- VSC extensions installation (on remote container) and configuration
- Testing and code coverage framework

You may customize your environment by updating Dockerfile, installed Python packages (requirements.txt) of VSC settings.

If you mess up your environment don't worry. Just rebuild the container.

## How to get it running
1. Install Docker Desktop ([download][7])
1. Install MS Visual Source Code ([download][8])
1. Clone ricardojamaia/ml-python-container GitHub repository
    1. View -> Command Pallete ...
    1. Type and select 'Git Clone'
    1. Enter 'https://github.com/ricardojamaia/ml-python-container.git'
    1. VS Code will prompt you to open the repository
1. Open repository in VS Code
1. Install 'Remote - Containers' VS Code extension
    1. VS Code will propmt you to install the recommended extensions i.e. Remote - Containers (ms-vscode-remote.remote-containers)
    1. If necessary search it manually on marketplace
    1. Click on install
1. Reopen in Container
    1. VS Code will detect a .devcontainer folder and prompt you to reopen the folder in container
    1. Reopen folder in container
  
That's it you should be able to start coding.

[1]: https://numpy.org/
[2]: https://matplotlib.org/
[3]: https://www.tensorflow.org/
[4]: http://scikit-learn.org
[5]: https://pytorch.org/
[6]: https://pandas.pydata.org/
[7]: https://www.docker.com/products/docker-desktop
[8]: https://code.visualstudio.com/download
