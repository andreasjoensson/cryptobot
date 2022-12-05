#!/usr/bin/python3.7
from binance.spot import Spot
import os
from twilio.rest import Client as twil
import schedule
import time
from binance.error import ClientError
proxies = {"http":"165.225.194.184:10034"}

client = Spot(proxies=proxies,key='', secret='')

account_sid = ''
auth_token = ''
twillio_client = twil(account_sid, auth_token)

def withdrawCrypto():
 xrpAsset = client.user_asset(asset='XRP')
 xrp = int(float(xrpAsset[0]['free'] if len(xrpAsset) > 0 else 0))
 btcAsset = client.user_asset(asset='BTC')
 btc = float(btcAsset[0]['free'] if len(btcAsset) > 0 else 0)
 solAsset = client.user_asset(asset='SOL')
 sol = float(solAsset[0]['free'] if len(solAsset) > 0 else 0)
 ethAsset = client.user_asset(asset='ETH')
 eth = float(ethAsset[0]['free'] if len(ethAsset) > 0 else 0)

 withdrawBitcoin(cryptoAmount=btc)
 withdrawEth(cryptoAmount=eth)
 withdrawSol(cryptoAmount=sol)
 withdrawXrp(cryptoAmount=xrp)

def buyCrypto():
  buyBTC(amount=20)
  buySOL(amount=20)
  buyXRP(amount=20)
  buyETH(amount=20)

def buyBTC(amount):
 params = {
    'symbol': 'BTCEUR',
    'side': 'BUY',
    'type': 'MARKET',
    'quoteOrderQty': amount,
 }
 try:
  response = client.new_order(**params)
  if response['status'] == 'FILLED':
   twillio_client.messages.create(
        body=f"Du har købt {response['executedQty']} BTC, som bliver sendt til din ledger om en halv time.",
        from_='+16203191851',
        to='+4522156649'
     )
 except ClientError as error:
  twillio_client.messages.create(
        body= "Der sket en fejl og den har ikke købt BTC. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        ),
        from_='+16203191851',
        to='+4522156649'
     )

def buyXRP(amount):
 params = {
    'symbol': 'XRPEUR',
    'side': 'BUY',
    'type': 'MARKET',
    'quoteOrderQty': amount,
 }

 try: 
  response = client.new_order(**params)
  if response['status'] == 'FILLED':
   twillio_client.messages.create(
        body=f"Du har købt {response['executedQty']} XRP, som bliver sendt til din ledger om en halv time.",
        from_='+16203191851',
        to='+4522156649'
     )
 except ClientError as error:
  twillio_client.messages.create(
        body= "Der sket en fejl og den har ikke købt XRP. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        ),
        from_='+16203191851',
        to='+4522156649'
     )

def buySOL(amount):
 params = {
    'symbol': 'SOLEUR',
    'side': 'BUY',
    'type': 'MARKET',
    'quoteOrderQty': amount,
 }

 response = client.new_order(**params)
 try:
  if response['status'] == 'FILLED':
   twillio_client.messages.create(
        body=f"Du har købt {response['executedQty']} SOL, som bliver sendt til din ledger om en halv time.",
        from_='+16203191851',
        to='+4522156649'
     )
 except ClientError as error:
   twillio_client.messages.create(
        body= "Der sket en fejl og den har ikke købt SOL. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        ),
        from_='+16203191851',
        to='+4522156649'
     )


def buyETH(amount):
 params = {
    'symbol': 'ETHEUR',
    'side': 'BUY',
    'type': 'MARKET',
    'quoteOrderQty': amount,
 }

 try: 
  response = client.new_order(**params)
  if response['status'] == 'FILLED':
   twillio_client.messages.create(
        body=f"Du har købt {response['executedQty']} ETH, som bliver sendt til din ledger om en halv time.",
        from_='+16203191851',
        to='+4522156649'
     )
 except ClientError as error:
   twillio_client.messages.create(
        body= "Der sket en fejl og den har ikke købt ETH. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        ),
        from_='+16203191851',
        to='+4522156649'
     )

def withdrawBitcoin(cryptoAmount):
  if cryptoAmount > 0.00100000000000000000: 
    try:
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
    except ClientError as error:
     twillio_client.messages.create(
        body= "Der sket en fejl og den har ikke kunnet udbetale BTC til din Ledger. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        ),
        from_='+16203191851',
        to='+4522156649'
     )


def withdrawEth(cryptoAmount):
 if cryptoAmount > 0.00980000000000000000:
    try:
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
    except ClientError as error:
     twillio_client.messages.create(
        body= "Der sket en fejl og den har ikke kunnet udbetale ETH til din Ledger. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        ),
        from_='+16203191851',
        to='+4522156649'
     )


    
def withdrawXrp(cryptoAmount):
 if cryptoAmount > 0.000001:
   try:
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
   except ClientError as error:
     twillio_client.messages.create(
        body= "Der sket en fejl og den har ikke kunnet udbetale XRP til din Ledger. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        ),
        from_='+16203191851',
        to='+4522156649'
     )

def withdrawSol(cryptoAmount):
   if cryptoAmount > 0.013:
    try: 
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
    except ClientError as error:
     twillio_client.messages.create(
        body= "Der sket en fejl og den har ikke kunnet udbetale SOL til din Ledger. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        ),
        from_='+16203191851',
        to='+4522156649'
     )

schedule.every().day.at("20:00").do(buyCrypto)
schedule.every().day.at("20:30").do(withdrawCrypto)
while 1:
  schedule.run_pending()
  time.sleep(1)