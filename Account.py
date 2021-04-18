class Account(object):


    def __init__(self, web3) -> None:
        self.web3 = web3
    
    def check_balance(self, wallet_address):
        return self.web3.eth.get_balance('0x554D7f955c7C3936FedcF27e97137a04883f3bcF')
    
    def check_send_possibility(self, gas_price, eth_count, wallet_balance) -> bool:
        if wallet_balance - 21000 * int(gas_price) + eth_count >= 0:
            return True
        else:
            return False
    
    @staticmethod
    def change_commission(gas_price: int, factor: int) -> str:
        commission = gas_price * factor
        return commission

    def send_ether(self, eth_count, amount_in_ether, web3, wallet_address, commission):
        nonce = web3.eth.getTransactionCount(wallet_address)
        amount_in_wei = web3.toWei(amount_in_ether,'ether');
        tx = {
            'nonce': nonce,
            'to': '0x554D7f955c7C3936FedcF27e97137a04883f3bcF',
            'value': amount_in_wei,
            'gas': 2000000,
            'gasPrice': self.web3.toWei(change_commission, 'gwei'),
        }
        
        signed_txn = web3.eth.account.signTransaction(txn_dict, wallet_private_key)
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print('tx_hash: {}'.format(tx_hash.hex()))
        txn_receipt = None
        count = 0
        while txn_receipt is None and (count < 30):

            txn_receipt = web3.eth.getTransactionReceipt(txn_receipt)
            print(txn_receipt)
            time.sleep(10)
        
        if txn_receipt is None:
            return {'status': 'failed', 'error': 'timeout'}
        return {'status': 'added', 'txn_receipt': txn_receipt}

    def set_allowance(deployed_contract_address, wallet_address): 
        tx_hash = contract.functions.approve(wallet_address)