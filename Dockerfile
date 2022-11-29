#
# A Docker image for running the DANDI analysis scripts
#

FROM ubuntu:22.04
MAINTAINER p.gleeson@gmail.com

USER root

RUN apt-get update
RUN apt-get install -y git htop wget apt-utils
RUN apt-get install -y gnupg2

# Install Neurodebian repos
RUN wget -O- http://neuro.debian.net/lists/focal.de-fzj.libre | tee /etc/apt/sources.list.d/neurodebian.sources.list
RUN apt-key adv --recv-keys --keyserver hkps://keyserver.ubuntu.com 0xA5D32F012649A5A9
RUN apt-get update

RUN apt-get install -y git-annex-standalone


# Install additional Python dependencies
RUN apt-get install -y python3-pip
RUN pip install wheel

COPY ./requirements.txt $HOME/requirements.txt
RUN pip install --requirement requirements.txt
RUN pip install datalad

RUN pip list

# Some aliases

RUN echo '\n\nalias cd..="cd .."\nalias h=history\nalias ll="ls -alt"\nalias python=python3\nalias ipython=ipython3\nalias pip=pip3' >> ~/.bashrc

RUN echo "Built the Docker image!"
