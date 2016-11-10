FROM centos:centos7

RUN yum -y update
RUN yum -y groupinstall "Development Tools"
RUN yum -y install \
           kernel-devel \
           kernel-headers \
           gcc-c++ \
           patch \
           libyaml-devel \
           libffi-devel \
           autoconf \
           automake \
           make \
           libtool \
           bison \
           tk-devel \
           zip \
           wget \
           tar \
           gcc \
           zlib \
           zlib-devel \
           bzip2 \
           bzip2-devel \
           readline \
           readline-devel \
           sqlite \
           sqlite-devel \
           openssl \
           openssl-devel \
           git \
           gdbm-devel \
           python-devel\
					 vim

# Pythonのインストール
RUN cd /opt \
    && wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz \
    && tar xzvf Python-3.5.2.tgz && cd Python-3.5.2 \
    &&./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib" \
    && make \
    && make altinstall && cd /opt \
    && rm -f Python-3.5.2.tar.xz \
    && rm -rf Python-3.5.2/

# pipインストール
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.5 get-pip.py


RUN pip3 install PyMySQL

# RUN pip3 install virtualenv
# RUN python3.5 -m venv env
# RUN source /root/env/bin/activate

# ENV MYSQL_HOST mysql

ADD . /app
WORKDIR /app

CMD ["/bin/bash"]
