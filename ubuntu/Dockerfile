FROM ubuntu:16.04

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    gcc \
    git \
    libpq-dev \
    zip \
    wget \
    make \
    git \
    pkg-config \
    ssh \
    python3 \
    python3-dev \
    python3-pip \
    && apt-get autoremove \
    && apt-get clean



# pipインストール
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

# slackbotインストール
RUN pip3 install slackbot

CMD ["/bin/bash"]
