import account
from constants import *

class Chequing(account.Account):

    def __init__(self, name, amount):
        super().__init__(name, amount)
        self.type = 'Chequing'

    def post_cheque(self, amount):
        """check amount, then check balance, pay cheque if sufficient amount, else charge bounce fee"""
        if self.check_float(amount):
            if self._balance + odLimit >= amount:
                self._balance -= amount
            else:
                self.bounce_fee()


    def bounce_fee(self):
        """charge bounce fee"""
        print('Insufficient balance, charged bounced cheque fee.')
        self._balance -= odFee
        self.add_entry('Overdraft', odFee)

    def withdraw(self, amount):
        """check amount, then check balance, allow withdraw if sufficient amount"""
        if self.check_float(amount):
            if self._balance + odLimit >= amount:
                self._balance -= amount
                self.add_entry('withdraw', amount)
            else:
                print('Insufficient funds.')

    def charge_interest(self):
        """if balance less than 0, then charge interest"""
        if self._balance < 0:
            interest = self._balance * odInterest
            self._balance += interest
            self.add_entry('chg int ', interest)

    def __str__(self):
        """print self information"""
        return '{:<10} {:>7} {:>10} {}'.format(str(self.accName),str(self.accNum),str(self.balance),self.type)


if __name__ == '__main__':
    a = Chequing('david', 500000)
    a.deposit(200000.01)
    a.withdraw(12.5)
    a.withdraw(1000000)
    a.withdraw(-200000)
    a.withdraw('hello')
    print(a)
    a.show_transaction()
