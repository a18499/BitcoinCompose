#!/bin/bash

echo "create private network"

bitcoind -regtest -daemon –printtoconsole & > /logs1.txt

echo "join private network"
bitcoin-cli -regtest addnode bob onetry > /logs2.txt


sleep 10000


