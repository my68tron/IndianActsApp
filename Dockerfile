FROM python:3.8-alpine
LABEL maintainer="my68tron"

# Creating project directory as we cannot work in root
RUN mkdir /app

# Current working directory
WORKDIR /app

# Disable python buffering to see logs in real-time
ENV PYTHONUNBUFFERED 1

# Copy the requirements file to install packages
COPY ./requirements.txt /app/

# --no-cahce-dir so that docker file should should not keep binaries
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install -r requirements.txt

# Copy all the code files to the root
COPY ./ /app

# Create a user named 'user' to increse security and not run as root
# '-D' => user will only execute programs, dont create home dir
RUN adduser -D user

# Switch to the newly created user
USER user