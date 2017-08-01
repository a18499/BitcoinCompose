FROM bitcoindev

# Clone git repository
RUN git clone https://github.com/fgwitera/btcregretarget.git ~/bitcoin
WORKDIR /root/bitcoin

# Build bitcoin
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
