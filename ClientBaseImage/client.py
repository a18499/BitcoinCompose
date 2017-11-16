import thread
import os
import logging
import random
import time

logging.basicConfig(level=logging.INFO)


#create daemon
def  create_daemon():
    logging.info("Begin to Create Daemon")
    os.system('bitcoind -regtest -daemon')
    logging.info("create network complete")

#join pravite network
def join_network():
    logging.info("Begin to join pravite network")
    os.system('bitcoind -addnode=mybitcoin_a -regtest -daemon')
    logging.info("Begin to join pravite network complete")

#show information 
def show():
    logging.info("Test")

def generateblock(blocknumber):
    os.system('bitcoin-cli -regtest generate '+str(blocknumber))
    logging.info("generate "+str(blocknumber) +"block")

#get balance
def getbalance():
    os.system("bitcoin-cli -regtest getbalance")
#main flow

logging.info("Start main flow")
logging.info("Waiting 30 sec for master node up")

time.sleep( 30 )
logging.info("Join network ")
join_network()
logging.info("Join network complete")

while 1:
    #logging.info("server is running")
    #os.system('sleep 5')
    #logging.info("generate sleep time")
    #sleeptime = random.randint(0,15)
    #logging.info("sleeptime is  "+str(sleeptime))
    #os.system('sleep '+str(sleeptime))
    #blocknumber = random.randint(100,300)
    generateblock(1)
    #logging.info("getbalance")
    #getbalance()
