import json
from Crypto.Hash import SHA256
from transaction import Transaction
import time

class Block:
    """
    This is a simple abstraction of a block, which contains a timestamp, a transactions list, a nonce value to 
    perform the proof-of work and references to the previous and the current block itself.
    """
    def __init__(self, timestamp, transactions, previous_hash=""):
        self.timestamp = timestamp
        self.nonce = 0
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def encrypt(self, string):
        """
        Encodes a standard string to binary form and generates a new SHA256 object with it.

        Args:
            string: To be converted

        Returns:
            A string representing the hash in hexadecimal.
        """
        string = bytes(string, encoding='utf-8')
        hash = SHA256.new()
        hash.update(string)
        return hash.hexdigest()

    def calculate_hash(self):
        """
        Defines a new SHA256 hash based on all the attributes of the block.

        Returns: 
            A new string that represents the hash of the block.
        """
        return self.encrypt(self.previous_hash + str(self.timestamp) + 
                            json.dumps([transaction.as_dict() for transaction in self.transactions]) + 
                            str(self.nonce))

    def mine_block(self, difficulty):
        """
        Here we are going to set the difficult required to perform our proof-of-work,
        whereas 'difficulty' is meant to act as a hindrance on adding a block to the chain.
        With 'mining' blocks we are just seeking for a hash string with a certain preset of
        characters.

        Args:
            difficulty: Zero initial addicional characters to the hash be considered as valid 
        """
        while (self.hash[0:difficulty] != (difficulty*str.format("0"))):
            self.nonce += 1
            self.hash = self.calculate_hash()

        print("BLOCK MINED: {}".format(self.hash))



class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.pending_transactions = []
        self.mining_reward = 100

    def create_genesis_block(self):
        return Block(timestamp=1546300800, transactions=[Transaction()], previous_hash="0")

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def mine_pending_transactions(self, mining_reward_addr):
        """
        When a miner call this method, it will pass along its wallet address and if this successfully
        manage to mine this block then send the reward to this address.

        Args:
            mining_reward_addr: 
        """
        block = Block(round(1000 * time.time()), self.pending_transactions, self.get_latest_block().hash)
        block.mine_block(self.difficulty)

        print("Block successfully mined!")
        self.chain.append(block)

        self.pending_transactions = []


    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_balance_of_address(self, addr):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if (transaction.from_addr ==  addr):
                    balance -= transaction.amount
                if (transaction.to_addr == addr):
                    balance += transaction.amount
        return balance

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if (current_block.hash != current_block.calculate_hash()):
                return False
            if (current_block.previous_hash != previous_block.hash):
                return False
        return True
        
    def show(self, verify=False):
        separator = 100*"-"

        print(separator)
        for index, block in enumerate(self.chain):
            print("[Block {}]".format(index))
            for attribute, value in block.__dict__.items():
                print("{}: {}".format(attribute, value))
            print(separator)
        
        if (verify):
            print("Is this blockchain valid? " + ("Yes" if self.is_chain_valid() else "No"))