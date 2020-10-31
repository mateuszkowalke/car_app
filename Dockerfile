# Base Image
FROM python:3.8

# create and set working directory and environment
WORKDIR /app
ENV PYTHONUNBUFFERED 1
ADD requirements.txt /app
RUN pip3 install -r requirements.txt

# Add current directory code to working directory
ADD . /app

EXPOSE 8000