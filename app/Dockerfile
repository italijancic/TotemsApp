# pull official base image
FROM python:3.10.0b2
# FROM python:3.10.0b2-buster
# FROM python:3.10.0b2-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependecies
RUN apt-get update && apt-get install vim -y

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
# COPY ./entrypoint.sh .

# copy project ONLY FOR PRODUCTION
# in developḿent the files are bind mounted with the volume
# COPY . .

# run entrypoint.sh
# ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]