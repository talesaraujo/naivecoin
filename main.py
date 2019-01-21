from blockchain import *

def check_integrity(blockchain):
    print("Is blockchain valid? ", blockchain.is_chain_valid())
    print("")

def test():

    naivecoin = Blockchain()
    naivecoin.add_block(Block(1, "18/01/2019", { "amount": 4 }))
    naivecoin.add_block(Block(2, "19/01/2019", { "amount": 10 }))
    naivecoin.add_block(Block(3, "20/01/2019", { "amount": 10 }))
    naivecoin.add_block(Block(4, "20/01/2019", { "amount": 7 }))

    naivecoin.show()
    check_integrity(naivecoin)

    # Try to tamper chain
    naivecoin.chain[2].data = { "amount": 1000}

    check_integrity(naivecoin)

if __name__ == '__main__':
    test()
