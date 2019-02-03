from blockchain import Block, Blockchain, Transaction

def check_integrity(blockchain):
    print("Is blockchain valid? ", blockchain.is_chain_valid())
    print("")

def test():

    naivecoin = Blockchain()
    naivecoin.create_transaction(Transaction('address-1', 'address-2', 100))
    naivecoin.create_transaction(Transaction('address-2', 'address-1', 50))

    print('\nStarting the miner...')
    naivecoin.mine_pending_transactions('address-of-mine')

    print('\nBalance of mine is {}'.format(naivecoin.get_balance_of_address('address-of-mine')))

if __name__ == '__main__':
    test()
