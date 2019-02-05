from blockchain import Block, Blockchain, Transaction

def check_integrity(blockchain):
    print("Is blockchain valid? " + ("Yes" if blockchain.is_chain_valid() else "No"))
    print("")

def main():

    naivecoin = Blockchain()

    naivecoin.create_transaction(Transaction('address-1', 'address-2', 100))
    naivecoin.create_transaction(Transaction('address-2', 'address-1', 50))

    check_integrity(naivecoin)

    print('\nStarting the miner...')
    naivecoin.mine_pending_transactions('me')

    print('\nMy current balance is {}'.format(naivecoin.get_balance_of_address('me')))

    check_integrity(naivecoin)

    print('\nRestarting the miner...')
    naivecoin.mine_pending_transactions('me')

    print('\nMy current balance is {}'.format(naivecoin.get_balance_of_address('me')))

    check_integrity(naivecoin)

    

if __name__ == '__main__':
    main()
    
