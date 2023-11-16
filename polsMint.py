from web3 import Web3
from dotenv import load_dotenv
import os
load_dotenv()

private_key = os.environ.get('account_private_key')
adress = os.environ.get('account_address')
rpc_url = "https://1rpc.io/matic"
web3 = Web3(Web3.HTTPProvider(rpc_url))
print(web3.is_connected()) 
print(Web3.from_wei(web3.eth.get_balance(adress),'ether')) 
c=0
while True:
    nonce = web3.eth.get_transaction_count(adress)
    tx = {
        'nonce': nonce,
        'chainId': 137,
        'to': adress, 
        'from':adress,
        'data':'0x646174613a2c7b2270223a227072632d3230222c226f70223a226d696e74222c227469636b223a22706f6c73222c22616d74223a22313030303030303030227d', #mint 16进制数据
        'gasPrice': web3.eth.gas_price,
        'value': Web3.to_wei(0, 'ether') 
    }
    try:
        gas = web3.eth.estimate_gas(tx) 
        tx['gas'] = gas 
        print(tx)
        signed_tx = web3.eth.account.sign_transaction(tx,private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(web3.to_hex(tx_hash))
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        if receipt.status == 1:
            c = c+1
            print("%s Mint Success!" %c)
            continue
        else:
            continue
    except Exception as e:
        print(e)
