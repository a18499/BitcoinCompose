#!/bin/bash

echo "create private network"

bitcoind -regtest -daemon -server

while :
do
        sleep 1
done
