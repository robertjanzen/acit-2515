# account.py
#
# Bank account program
#
# Robert Janzen A01029341 2B

from transaction_log import TransactionLog

class Account():

    _NEXT_ACCT_NUM = 10000

    def __init__(self, name, balance):
        self.account_number = Account._NEXT_ACCT_NUM
        self.account_holder_name = name
        self._balance = balance
        self.min_balance = 0
        self.transaction_log = TransactionLog(self.account_number)
        Account._NEXT_ACCT_NUM += 1

    def __str__(self):
        return 'Name: {0}\nAccount Number: {1}\nBalance: {2}'.format(self.account_holder_name, self.account_number, self.balance)

    def withdraw(self, amount):
        if amount >= 0.0:
            check_bal = self._balance - float(amount)
        else:
            print('withdrawal must be more than $0.00')
            return

        if check_bal >= self.min_balance:
            self._balance -= float(amount)
            self.transaction_log.save('Withdrawal', float(amount), self.account_number)
        else:
            print('Insufficient funds')
        return

    def deposit(self, amount):
        try:
            float(amount)
        except:
            raise TypeError("Amount is not a float")

        if amount >= 0.0:
            self._balance += float(amount)
            self.transaction_log.save('Deposit', amount, self.account_number)
        else:
            print('deposit must be more than $0.00')
        return

    def change_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")

        oldname = self.account_holder_name
        self.account_holder_name = new_name
        self.transaction_log.save('Name Change', oldname+'-'+new_name, self.account_number)
        return

    @property
    def balance(self):
        return self._balance

if __name__ == '__main__':
    print('account.py...')