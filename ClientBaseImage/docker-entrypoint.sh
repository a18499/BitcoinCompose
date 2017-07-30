#!/bin/bash

# git clone https://github.com/bitcoin/bitcoin.git ~/bitcoin
# cd ~/bitcoin
# git checkout v0.14.0rc3
# 
# ./autogen.sh
# ./configure
# make
# make install

echo "create private network"

bitcoind -regtest -daemon

sleep 3

echo "join private network"
bitcoin-cli -regtest addnode bob onetry

python client.py



