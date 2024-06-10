FROM docker:20.10-dind

ENV NODE_OPTIONS="--openssl-legacy-provider"


MAINTAINER p.gleeson@gmail.com

USER root

RUN apk update
RUN apk add git htop wget gnupg sudo



RUN mkdir -p /etc/apk/sources.list.d/
RUN mkdir $HOME/testing/
RUN mkdir $HOME/tmp/

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
RUN apk add py3-pandas


COPY ./requirements.txt $HOME/requirements.txt

# RUN git clone --branch development https://github.com/MetaCell/nwb-explorer
# RUN pip install --editable nwb-explorer
# RUN python nwb-explorer/utilities/install.py --npm-skip

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

RUN git clone https://github.com/OpenSourceBrain/OSBv2.git -b dev_test_nwbdocker
RUN sed -i '27d;27i\RUN mkdir /home/jovyan/nwb-explorer/tmp' OSBv2/applications/nwb-explorer/Dockerfile

WORKDIR /tmp
#RUN datalad install -s https://github.com/dandi/dandisets.git --recursive --recursion-limit 1 --jobs 4
RUN datalad install -s https://github.com/dandi/dandisets.git
RUN cd dandisets; ls -alt ./tools/list-matching-access-status; /bin/sh -e tools/list-matching-access-status public
RUN cd dandisets; ls -alt tools; /bin/sh -e tools/list-matching-access-status public | xargs datalad install  --recursive --recursion-limit 1 --jobs 4
WORKDIR / 

RUN echo "Built the Docker image!"
