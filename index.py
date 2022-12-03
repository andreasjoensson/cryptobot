#!/usr/bin/python3.7
from binance.spot import Spot
import os
from twilio.rest import Client as twil
import schedule
import time
proxies = {"http":"165.225.194.184:10034"}

client = Spot(proxies=proxies,key='', secret='')
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ''
auth_token = ''
twillio_client = twil(account_sid, auth_token)

def checkBalance():
 xrpAsset = client.user_asset(asset='XRP')
 xrp = int(float(xrpAsset[0]['free'] if len(xrpAsset) > 0 else 0))
 btcAsset = client.user_asset(asset='BTC')
 btc = float(btcAsset[0]['free'] if len(btcAsset) > 0 else 0)
 solAsset = client.user_asset(asset='SOL')
 sol = float(solAsset[0]['free'] if len(solAsset) > 0 else 0)
 ethAsset = client.user_asset(asset='ETH')
 eth = float(ethAsset[0]['free'] if len(ethAsset) > 0 else 0)
 withdrawBitcoin(cryptoAmount=btc)

# withdraw 100 ETH
def withdrawBitcoin(cryptoAmount):
  if cryptoAmount > 0.00100000000000000000: 
    result = client.withdraw(
        coin='BTC',
        address='bc1qu0j2y7t87p20t7ywk2n0wy4sm8zg2y3myk3rud',
        amount=cryptoAmount,
        )
    if result['id']:
     twillio_client.messages.create(
        body=f"Der er blevet sendt {cryptoAmount} BTC til din Ledger",
        from_='+16203191851',
        to='+4522156649'
     )
    else:
      twillio_client.messages.create(
        body=f"Der er sket en fejl og BTC blir ik sendt til din Ledger",
        from_='+16203191851',
        to='+4522156649'
     )


def withdrawEth(cryptoAmount):
 if cryptoAmount > 0.00980000000000000000:
    result = client.withdraw(
        coin='ETH',
        address='0xF2a8b5262390caB34B2Abe967E88b055f7Ef1696',
        amount=cryptoAmount)
    if result['id']:
      twillio_client.messages.create(
        body=f"Der er blevet sendt {cryptoAmount} ETH til din Ledger",
        from_='+16203191851',
        to='+4522156649'
     )
    else:
      twillio_client.messages.create(
        body=f"Der er sket en fejl og ETH blir ik sendt til din Ledger",
        from_='+16203191851',
        to='+4522156649'
     )


    
def withdrawXrp(cryptoAmount):
 if cryptoAmount > 0.000001:
    print('XRP ER STØRRE')
    result = client.withdraw(
        coin='XRP',
        address='r3hJSdaWaG2CzJnhLLUL9QoPpysjbc9utx',
        amount=cryptoAmount)
    if result['id']:
      twillio_client.messages.create(
        body=f"Der er blevet sendt {cryptoAmount} XRP til din Ledger",
        from_='+16203191851',
        to='+4522156649'
     )
    else:
      twillio_client.messages.create(
        body=f"Der er sket en fejl og XRP blir ik sendt til din Ledger",
        from_='+16203191851',
        to='+4522156649'
     )

def withdrawSol(cryptoAmount):
   if cryptoAmount > 0.013:
    result = client.withdraw(
        coin='SOL',
        address='4NgqRcdynZsbhFUiye9d2EPuUdE8QEaLZvGu8eTZF1t3',
        amount=cryptoAmount)
    if result['id']:
      twillio_client.messages.create(
        body=f"Der er blevet sendt {cryptoAmount} SOL til din Ledger",
        from_='+16203191851',
        to='+4522156649'
     )
    else:
      twillio_client.messages.create(
        body=f"Der er sket en fejl og SOL blir ik sendt til din Ledger",
        from_='+16203191851',
        to='+4522156649'
     )


checkBalance()
schedule.every().day.at("00:48").do(checkBalance)
while 1:
  schedule.run_pending()
  time.sleep(1)