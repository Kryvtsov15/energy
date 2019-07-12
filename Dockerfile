FROM python:3.7
MAINTAINER Kryvtsov
ENV PYTHONUNBUFFERED 1
RUN mkdir /energy
WORKDIR /energy

COPY req.txt /energy/
RUN pip install -r req.txt


COPY . /energy/
