# chequing.py
#
# Bank account program
#
# Robert Janzen A01029341 2B

from account import Account

class Chequing(Account):

    BOUNCE_FEE = 25.0

    def __init__(self, name, balance=0, overdraft=500, interest_rate=0, overdraft_interest_rate=0.03):
        super().__init__(name, balance)
        self.overdraft = overdraft
        self.interest_rate = interest_rate
        self.min_balance = overdraft * -1
        self.overdraft_interest_rate = overdraft_interest_rate

    def post_cheque(self, amount):
        if amount >= 0.0:
            check_bal = self._balance - float(amount)
        else:
            print('Cheque value must be more than $0.00')
            return

        if check_bal >= self.min_balance:
            self._balance -= float(amount)
            self.transaction_log.save('Post Cheque', float(amount), self.account_number)
        else:
            self.bounce_fee()
            print('Insufficient funds')
        return

    def charge_overdraft_interest(self):
        if self._balance < 0:
            self._balance = self._balance * (self.overdraft_interest_rate + 1)
            self.transaction_log.save('Charge Overdraft Interest', (self._balance * (self.overdraft_interest_rate + 1)), self.account_number)
        return

    def bounce_fee(self):
        self._balance -= Chequing.BOUNCE_FEE
        self.transaction_log.save('Bounce Fee', Chequing.BOUNCE_FEE, self.account_number)
        return

if __name__ == '__main__':
    print('chequing.py...')
    ch1 = Chequing('Bob')
    ch1.deposit(200.0)
    ch1.post_cheque(150.0)
    ch1.withdraw(100.0)
    ch1.withdraw(500.0)