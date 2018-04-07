from saving import Saving
import datetime
from constants import *

class TermSaving(Saving):

    def __init__(self, name, amount):
        """constructor, inherits from super"""
        super().__init__(name, amount)
        self.type = 'Term Saving'
        self.depList = []
        self.deposit_date(amount)
        self.avaBal = 0

    def deposit_date(self, amount, date=datetime.date.today()):
        """method to keep track of recent deposits"""
        self.depList.append((date + datetime.timedelta(days=termDay), amount))

    def deposit(self, amount):
        """method to deposit, updates list, check available balance, and transaction log"""
        if self.check_float(amount):
            self._balance += amount
            self.deposit_date(amount)
            self.check_avaBal()
            self.add_entry('deposit', amount)

    def check_avaBal(self, date=datetime.date.today()):
        """method to check and update available balance"""
        for i in self.depList:
            if i[0] <= date:
                self.avaBal += i[1]
                self.depList.remove(i)

    def withdraw(self, amount):
        """method to withdraw amount and update"""
        if self.check_float(amount):
            self.check_avaBal()
            if amount <= self.avaBal:
                self._balance -= amount
                self.avaBal -= amount
                self.add_entry('withdraw', amount)
            else:
                print('Insufficient available balance to withdraw {}'.format(amount))


if __name__ == '__main__':
    a = TermSaving('david', 5000)
    a.deposit(2000)
    print(a.depList)
    a.check_avaBal(datetime.date.today() + datetime.timedelta(days=60))
    a.withdraw(2555)
    print(a.avaBal)