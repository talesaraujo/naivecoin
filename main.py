from blockchain import *

def main():

    dumbcoin = Blockchain()
    dumbcoin.add_block(Block(1, "18/01/2019", { "amount": 4 }))
    dumbcoin.add_block(Block(2, "19/01/2019", { "amount": 10 }))

    dumbcoin.show()
    print("Is blockchain valid? ", dumbcoin.is_chain_valid())
    print("")

    dumbcoin.chain[1].data = { "amount": 100 }

    dumbcoin.show()
    print("Is blockchain valid? ", dumbcoin.is_chain_valid())
    print("")

    dumbcoin.chain[1].calculate_hash()

    dumbcoin.show()
    print("Is blockchain valid? ", dumbcoin.is_chain_valid())
    print("")

if __name__ == '__main__':
    main()
