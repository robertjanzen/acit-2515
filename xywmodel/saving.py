import account
from constants import *

class Saving(account.Account):

    def __init__(self, name, amount):
        super().__init__(name, amount)
        self.type = 'Saving'

    def charge_fee(self):
        """charges fee if balance is below minimum"""
        if self._balance < savMin:
            self._balance -= savFee
            self.add_entry('pay int ', savFee)

    def pay_interest(self):
        """pay interest if maintaining the minimum balance"""
        if self._balance >savMin:
            interest = self._balance * savInterest
            self._balance += interest
            self.add_entry('pay int ', interest)

    def __str__(self):
        """prints out account information"""
        return '{:<10} {:>7} {:>10} {}'.format(str(self.accName),str(self.accNum),str(self.balance),self.type)

if __name__ == '__main__':
    a = Saving('david', 500000)
    print(a)