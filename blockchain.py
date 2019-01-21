import json
from Crypto.Hash import SHA256

class Block:
    """
    This is a simple abstraction of a block, which contains an index,
    a timestamp, a field representing data in general, and references
    for the previous and the current block itself.
    """
    def __init__(self, index, timestamp, data, previous_hash=""):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def encrypt(self, string):
        string = bytes(string, encoding='utf-8')
        hash = SHA256.new()
        hash.update(string)
        return hash.hexdigest()

    def calculate_hash(self):
        return self.encrypt(str(self.index) + self.previous_hash + self.timestamp + json.dumps(self.data))


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(index=0, timestamp="01/01/2019", data="Genesis Block", previous_hash="0")

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

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
