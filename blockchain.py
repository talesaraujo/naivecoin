import json
from Crypto.Hash import SHA256
from transactions import Transaction
import datetime

class Block:
    """
    This is a simple abstraction of a block, which contains an index,
    a timestamp, a field representing data in general, and references
    for the previous and the current block itself.
    """
    def __init__(self, timestamp, transactions, previous_hash=""):
        self.timestamp = timestamp
        self.nonce = 0
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def encrypt(self, string):
        string = bytes(string, encoding='utf-8')
        hash = SHA256.new()
        hash.update(string)
        return hash.hexdigest()

    def calculate_hash(self):
        return self.encrypt(str(self.index) + self.previous_hash + self.timestamp + json.dumps(self.data) + str(self.nonce))

    def mine_block(self, difficulty):
        """
        Here we are going to set the difficult required to perform our proof-of-work,
        whereas 'difficulty' is meant to act as a hindrance on adding a block to the chain.
        With 'mining' blocks we are just seeking for a hash string with a certain preset of
        characters.
        """
        while (self.hash[0:difficulty] != (difficulty*str.format("0"))):
            self.nonce += 1
            self.hash = self.calculate_hash()

        print("Block mined: {}".format(self.hash))


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions = []
        self.mining_reward = 100

    def create_genesis_block(self):
        return Block(timestamp="01/01/2019", transactions="Genesis Block", previous_hash="0")

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def mine_pending_transactions(self, mining_reward_addr):
        """
        Implement mine_pending_transactions method
        """
        
        block = Block()



    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if (current_block.hash != current_block.calculate_hash()):
                return False
            if (current_block.previous_hash != previous_block.hash):
                return False
        return True

    def show(self):
        for block in self.chain:
            for attribute, value in block.__dict__.items():
                print("{}: {}".format(attribute, value))
            print("")
