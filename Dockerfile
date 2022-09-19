#Create a ubuntu base image with python 3 installed.
FROM python:3.7-buster

# Set environment varibles
ENV PYTHONDONTWRITEBYTECDE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP manage.py
ENV BB_PASS=sqqjhcUxw7Ht9qTKLLS6
ENV BB_USERNAME=cwaithaka

#Set the working directory
RUN mkdir /app
WORKDIR /app

#Install the dependencies
RUN apt-get -y update

# install requirements
RUN pip install --upgrade pip==20.3.3
#COPY payments_consumer/requirements.txt .
ADD requirements.txt /app
RUN pip3 install -r /app/requirements.txt
RUN pip3 install git+https://${BB_USERNAME}:${BB_PASS}@bitbucket.org/copiadev/utilities.git@v3.10.2

COPY . .

#Expose the required port
# EXPOSE 5000
