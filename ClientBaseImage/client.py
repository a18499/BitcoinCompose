import thread
import os
import logging

logging.basicConfig(level=logging.INFO)


#create daemon
def  create_daemon():
    logging.info("Begin to Create Daemon")
    os.system('bitcoind -regtest -daemon')
    logging.info("create network complete")

#join pravite network
def join_network():
    logging.info("Begin to join pravite network")
    os.system('bitcoin-cli -regtest addnode bob onetry')
    logging.info("Begin to join pravite network complete")

#show information 
def show():
    logging.info("Test")

def generateblock():
    os.system('bitcoin-cli -regtest generate 100')
    logging.info("generate 100 block")

#get balance
def getbalance():
    os.system("bitcoin-cli -regtest getbalance")
#main flow
logging.info("Start main flow")
os.system('sleep 5')
generateblock()


while 1:
    logging.info("server is running")
    os.system('sleep 5')
    logging.info("getbalance")
    getbalance()