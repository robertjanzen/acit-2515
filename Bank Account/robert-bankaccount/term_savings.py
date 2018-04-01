# term_savings.py
#
# Bank account program
#
# Robert Janzen A01029341 2B

from savings import Savings
from term_deposits import TermDeposits

class TermSavings(Savings):

    def __init__(self, name, balance=0):
        super().__init__(name, balance)
        self.term_deposits = TermDeposits(self.account_number)

    def deposit(self, amount):
        super().deposit(amount)
        self.term_deposits.save(amount, self.account_number)

    def withdraw(self, amount):
        funds_availabe = self.term_deposits.calc_valid_amount()
        if funds_availabe >= amount:
            super().withdraw(amount)
        else:
            print('No funds available')
        return

if __name__ == '__main__':
    print('term_savings.py...')
