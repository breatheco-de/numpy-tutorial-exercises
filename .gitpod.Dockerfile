FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install pytest==4.6.0 pytest-testdox mock numpy==1.17.4 pandas==0.25.3 jupyter==1.0.0 jupyterthemes==0.20.0 mdutils==1.0.0 && npm i @learnpack/learnpack -g && learnpack plugins:install learnpack-python@0.0.35