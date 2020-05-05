FROM python:3.8-alpine
LABEL maintainer="my68tron"

# WORKDIR /app

# Disable python buffering to see logs in real-time
ENV PYTHONUNBUFFERED 1

COPY ./Pipfile.lock /

# --no-cahce-dir so that docker file should should not keep binaries
RUN pip install --no-cache-dir -r requirements.txt

# Create a user named 'user' to increse security and not run as root
# '-D' => user will only execute programs, dont create home dir
RUN adduser -D user

# Switch to the newly created user
USER user