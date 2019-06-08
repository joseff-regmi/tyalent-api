# Dockerfile -> Docker Client -> Docker Server(Daemon) -> Usable Image
# Use an existing docker image as a base
FROM python:3.7-alpine
# The name of this image(through Dockerfile) maintainer
LABEL Tushant Khatiwada

# tells python to run unbuffered mode which is recommended when running within python docker container
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set working directory which will be inside ubuntu
WORKDIR /code

#### Install a dependency ####

# Copies new files and resources to the image's filesystems
RUN pip3 install pipenv
COPY Pipfile Pipfile.lock /code/
RUN ls /etc/apk/
RUN echo "https://mirror.csclub.uwaterloo.ca/alpine/v3.9/main" > /etc/apk/repositories
RUN echo "https://mirror.csclub.uwaterloo.ca/alpine/v3.9/community" >>/etc/apk/repositories
RUN apk update
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pipenv install --system
# RUN apk del .tmp-build-deps
COPY . /code/

RUN adduser -D user
USER user
# Tell the image what to do when it starts as a container