#!/bin/bash

echo "create private network"

bitcoind -regtest -daemon

sleep 1000

echo "join private network"
bitcoin-cli -regtest addnode bob onetry
