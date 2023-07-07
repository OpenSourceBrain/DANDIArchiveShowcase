FROM docker:dind

MAINTAINER p.gleeson@gmail.com

USER root

RUN apk update
RUN apk add git htop wget gnupg
RUN mkdir -p /etc/apk/sources.list.d/
RUN mkdir $HOME/testing/

# Install Neurodebian repos
RUN wget -O- http://neuro.debian.net/lists/focal.de-fzj.libre | tee /etc/apk/sources.list.d/neurodebian.sources.list


RUN gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 0xA5D32F012649A5A9


RUN apk update

RUN apk add g++ postgresql-dev cargo gcc python3-dev libffi-dev musl-dev zlib-dev jpeg-dev build-base sed

RUN apk add git-annex

# Install additional Python dependencies
RUN apk add python3 py3-pip
RUN pip install --upgrade pip setuptools wheel
RUN apk update && apk add --no-cache hdf5-dev
RUN pip install h5py

COPY ./requirements.txt $HOME/requirements.txt
#RUN pip install --extra-index-url https://alpine-wheels.github.io/index numpy
RUN pip install --requirement requirements.txt
RUN pip install datalad

RUN pip list

RUN git config --global user.email "github_ci@test.test"
RUN git config --global user.name "github ci"

ENV DOCKER_HOST: tcp://thedockerhost:2375/

# Some aliases
RUN echo '\n\nalias cd..="cd .."\nalias h=history\nalias ll="ls -alt"\nalias python=python3\nalias ipython=ipython3\nalias pip=pip3' >> ~/.bashrc

RUN pip install --upgrade numpy

RUN git clone https://github.com/OpenSourceBrain/OSBv2.git
RUN sed -i '27d' OSBv2/applications/nwb-explorer/Dockerfile

RUN echo "Built the Docker image!"
