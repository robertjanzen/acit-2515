from logentry import Transaction

class Translog():
    def __init__(self):
        """this initializes a new log object for an account"""
        self.list = []

    def add_entry(self, accNum, type, tx_amount):
        """this method adds a line of string to the log"""
        self.list.append(Transaction(accNum, type, tx_amount))