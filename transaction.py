class Transaction(object):
    def __init__(self, from_addr, to_addr, amount):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.amount = amount

    def as_dict(self):
        return {'from': self.from_addr, 'to': self.to_addr, 'amount': self.amount}
