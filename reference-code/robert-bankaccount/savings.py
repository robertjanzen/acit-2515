# savings.py
#
# Bank account program
#
# Robert Janzen A01029341 2B

from account import Account

class Savings(Account):

    MIN_BALANCE_FEE = 10.0

    def __init__(self, name, balance=0, interest_rate=0.02, minimum_balance=1000.0):
        super().__init__(name, balance)
        self.interest_rate = interest_rate
        self.minimum_balance = minimum_balance

    def charge_min_balance_fee(self):
        self._balance -= Savings.MIN_BALANCE_FEE
        self.transaction_log.save('Min Balance Fee', Savings.MIN_BALANCE_FEE, self.account_number)
        return

    def pay_interest(self):
        if self._balance >= self.min_balance:
            self._balance *= (self.interest_rate + 1)
            self.transaction_log.save('Pay Interest', self._balance*(self.interest_rate+1), self.account_number)
        return

if __name__ == '__main__':
    print('savings.py...')