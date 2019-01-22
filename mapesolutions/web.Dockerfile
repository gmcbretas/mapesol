FROM ubuntu:latest
ENV PYTHONUNBUFFERED 1
RUN apt-get update
#Locales
RUN apt-get install -yq locales -qq
ENV LANGUAGE pt_BR
ENV LANG=pt_BR
ENV LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
RUN locale-gen pt_BR pt_BR.UTF-8; dpkg-reconfigure locales
RUN apt-get update
RUN apt-get --assume-yes install python3-pip
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip3 install -r requirements.txt
ADD . /code

