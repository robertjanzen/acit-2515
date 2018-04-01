# term_deposits.py
#
# Bank account program
#
# Robert Janzen A01029341 2B

from deposit import Deposit
from datetime import datetime
from datetime import timedelta

class TermDeposits():

    def __init__(self, account_number, deposits=[]):
        self.account_number = account_number
        self.deposits = deposits

    def save(self, amount, acct_num):
        new_deposit = Deposit(amount, self.account_number)

        f = open(str(self.account_number)+'-term_deposits.txt', 'a+')
        f.write(new_deposit.toString()+'\n')
        f.close()
        return

    def calc_valid_amount(self):
        valid_amount = 0.0
        f = open(str(self.account_number)+'-term_deposits.txt', 'r')
        for line in [line.rstrip() for line in f.readlines()]:

            # Compare against the valid date at the end of each deposit log
            if (datetime.strptime(line.split(',')[-1], '%Y-%m-%d %H:%M:%S.%f') < (datetime.now() - timedelta(days=60))):
                valid_amount += float(line.split(',')[2])

        f.close()
        return valid_amount

    def list_deposits(self):
        f = open(str(self.account_number)+'-term_deposits.txt', 'r')
        for line in [line.rstrip() for line in f.readlines()]:
            print(line)
        return

if __name__ == '__main__':
    print('term_deposits.py...')