# deposit.py
#
# Bank account program
#
# Robert Janzen A01029341 2B

from datetime import datetime
from datetime import timedelta

class Deposit():

    def __init__(self, amount, acct_num, deposit_date=str(datetime.now())):
        self.amount = amount
        self.acct_num = acct_num
        self.deposit_date = deposit_date
        self.withdraw_date = datetime.now() + timedelta(days=60)

    def __str__(self):
        return str(self.deposit_date)+','+str(self.acct_num)+','+str(self.amount)+','+str(self.withdraw_date)

    def toString(self):
        return str(self.deposit_date)+','+str(self.acct_num)+','+str(self.amount)+','+str(self.withdraw_date)

if __name__ == '__main__':
    print('deposit.py...')