FROM bitcoindev

# Clone git repository
RUN git clone https://github.com/bitcoin/bitcoin.git ~/bitcoin
WORKDIR /root/bitcoin
RUN git checkout v0.14.0rc3

# Build bitcoin
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
