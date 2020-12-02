FROM alpine:latest

ARG terraform_version="0.13.5"

# install terraform.
RUN wget https://releases.hashicorp.com/terraform/${terraform_version}/terraform_${terraform_version}_linux_amd64.zip && \
    unzip ./terraform_${terraform_version}_linux_amd64.zip -d /usr/local/bin/ && \
    rm ./terraform_${terraform_version}_linux_amd64.zip

# set time-zone=JST
RUN apk --update add tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata && \
    rm -rf /var/cache/apk/*

# create workspace.
COPY ./terraform /root/tf

# move to workspace
WORKDIR /root/tf
