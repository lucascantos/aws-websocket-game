FROM python:3.9-alpine

# Install OS dependencies
RUN apk update \
    && apk --no-cache add gcc libc-dev bash git npm openssh

# Alpine does not support binary Python wheels -> we need to compile cffi and cryptography.
RUN apk add musl-dev python3-dev libffi-dev openssl-dev cargo

# Set working directory
RUN mkdir -p /home/deploy/.ssh/ /home/deploy/app/
WORKDIR /home/deploy/app/

# Copy requirement files
COPY requirements* ./
COPY package.json ./

# Install packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN npm install
ENV PATH /home/deploy/app/node_modules/.bin:$PATH

# Make folder and copy files to it
COPY . /home/deploy/app/

# Set volume mounts
VOLUME /home/deploy/app/

# # Run serverless offline
# ENTRYPOINT ["/bin/bash"]
# CMD ["echo websocket"]
