#!/bin/bash

echo "create private network"

bitcoind -regtest -daemon –printtoconsole &

sleep 10000


