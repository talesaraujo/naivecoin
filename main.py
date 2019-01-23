from blockchain import *

def check_integrity(blockchain):
    print("Is blockchain valid? ", blockchain.is_chain_valid())
    print("")

def test():

    naivecoin = Blockchain()
        
    print("Mining block 1... ")
    naivecoin.add_block(Block(1, "18/01/2019", { "amount": 4 }))

    print("Mining block 2... ")
    naivecoin.add_block(Block(2, "19/01/2019", { "amount": 10 }))

    print("Mining block 3... ")
    naivecoin.add_block(Block(3, "20/01/2019", { "amount": 10 }))

    print("Mining block 4...")
    naivecoin.add_block(Block(4, "20/01/2019", { "amount": 7 }))


if __name__ == '__main__':
    test()
