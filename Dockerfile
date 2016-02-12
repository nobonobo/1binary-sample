FROM centos:6

# install python 3.4
RUN yum groupinstall -y 'development tools'; \
  yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel\
      readline-devel tk-devel gdbm-devel db4-devel
RUN python2 -c 'import sys, StringIO, tarfile, urllib;tarfile.open(fileobj=StringIO.StringIO(urllib.urlopen(sys.argv[1]).read())).extractall(sys.argv[2])' https://www.python.org/ftp/python/3.4.4/Python-3.4.4.tgz /
RUN cd /Python-3.4.4; ./configure && make && make altinstall && rm -r /Python-*

# install exxo
RUN yum install -y tar | true
RUN curl -L https://bintray.com/artifact/download/mbachry/exxo/exxo-0.0.5.tar.xz | tar xJvf - -C /usr/local/bin

RUN exxo venv /env
COPY ./src /src
WORKDIR /src
RUN source /env/bin/activate && exxo build
