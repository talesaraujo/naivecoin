from blockchain import Block, Blockchain, Transaction

def main():

    naivecoin = Blockchain()

    naivecoin.create_transaction(Transaction('address-1', 'address-2', 100))
    naivecoin.create_transaction(Transaction('address-2', 'address-1', 50))

    naivecoin.show(verify=True)

    print('\n\nStarting the miner...')
    naivecoin.mine_pending_transactions('me')
    print('\nMy current balance is {}'.format(naivecoin.get_balance_of_address('me')))

    naivecoin.show(verify=True)

    print('\n\nRestarting the miner...')
    naivecoin.mine_pending_transactions('me')
    print('\nMy current balance is now {}'.format(naivecoin.get_balance_of_address('me')))

    naivecoin.show(verify=True)



if __name__ == '__main__':
    main()
    
