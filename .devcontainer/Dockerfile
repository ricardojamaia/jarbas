# See here for image contents: https://github.com/microsoft/vscodewhic-dev-containers/tree/v0.145.1/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Install additional OS packages.
# 'ffmpeg', 'libsm6' and 'libxext6' are required by OpenCV
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends 'ffmpeg' \
    'libsm6'\ 
    'libxext6'

# Update pip
RUN pip3 install --upgrade pip

# Install additional pip packages. Add packages to requirements.txt
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp
