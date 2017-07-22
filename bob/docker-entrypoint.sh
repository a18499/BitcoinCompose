#!/bin/bash

echo "create private network"

bitcoind -regtest -daemon
sleep 1000
bitcoin-cli -regtest getinfo
