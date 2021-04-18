import json
import time
from web3 import Web3, HTTPProvider
from Account import Account

blockchain_address = 'http://127.0.0.1:7545/'
web3 = Web3(HTTPProvider(blockchain_address))
web3.eth.defaultAccount = web3.eth.accounts[0]

acc = Account(web3)

compiled_contract_path = 'build/contracts/HelloWorld.json'
deployed_contract_address = '0x2C0e5012D152D7e155AeF5CEE53c4Ea8dB675D03'
wallet_private_key = '8909666ec09a97c80ceb25bec0133a716ddb82daa23b786d563f45f6db9cb7b9'
wallet_address = '0x71BFc9D45aa1780A25EA9b4c690Fa52E78606900'

wallet_balance = web3.eth.get_balance('0x71BFc9D45aa1780A25EA9b4c690Fa52E78606900')
eth_count = 1
gas_price = web3.eth.gas_price
gas_price_commission = acc.change_commission(20, 3)
with open(compiled_contract_path) as file:
    contract_json = json.load(file) 
    contract_abi = contract_json['abi']  

if acc.check_send_possibility(gas_price, eth_count, wallet_balance):
    tr_hash = acc.send_ether(eth_count, wallet_balance, web3, wallet_address, gas_price_commission)