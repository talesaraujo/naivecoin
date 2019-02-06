class Transaction(object):
    def __init__(self, from_addr=None, to_addr=None, amount=0):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.amount = amount

    def __repr__(self):
        return "('from':{}, 'to':{}, 'amount':{})".format(self.from_addr, self.to_addr, self.amount)

    def as_dict(self):
        return {'from': self.from_addr, 'to': self.to_addr, 'amount': self.amount}
