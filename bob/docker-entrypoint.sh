#!/bin/bash

echo "create private network"

bitcoind -regtest -daemon -server
sleep 600
