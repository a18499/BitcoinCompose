FROM ubuntu:xenial

RUN apt-get -y update
RUN apt-get install -y python-software-properties 
RUN apt-get install -y software-properties-common

RUN add-apt-repository ppa:bitcoin/bitcoin
RUN apt-get -y update

# install some other essential packages for building bitcoin
RUN apt-get install --yes autoconf
RUN apt-get install --yes autotools-dev
RUN apt-get install --yes bsdmainutils
RUN apt-get install --yes build-essential
RUN apt-get install --yes gcc 
RUN apt-get install --yes git 
RUN apt-get install --yes libboost-all-dev
RUN apt-get install --yes libssl-dev
RUN apt-get install --yes libevent-dev
RUN apt-get install --yes libtool
RUN apt-get install --yes automake
RUN apt-get install --yes pkg-config
RUN apt-get install --yes libdb4.8
RUN apt-get install --yes libdb4.8++-dev

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Clone git repository
RUN git clone https://github.com/bitcoin/bitcoin.git ~/bitcoin
WORKDIR /root/bitcoin
RUN git checkout v0.14.0rc3

# Build bitcoin
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install

RUN mkdir ~/.bitcoin
RUN echo "rpcuser=test\nrpcpassword=test\nrpcallowip=0.0.0.0/0\n" > ~/.bitcoin/bitcoin.conf

RUN echo "alias rt='bitcoin-cli -regtest'" >> ~/.bashrc

COPY ./docker-entrypoint.sh /
COPY ./client.py /
WORKDIR /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]


