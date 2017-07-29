#!/bin/bash

echo "create private network"

bitcoind -regtest -daemon

sleep 1

echo "join private network"
bitcoin-cli -regtest addnode bob onetry

while : 
do
        sleep 1
done
