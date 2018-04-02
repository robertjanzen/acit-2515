# transaction.py
#
# Bank account program
#
# Robert Janzen A01029341 2B

import datetime
now = datetime.datetime.now()

class Transaction():

    def __init__(self, type, value, acct_num, date=str(now)):
        self.type = type
        self.value = value
        self.acct_num = acct_num
        self.date = date

    def __str__(self):
        return str(self.date)+','+str(self.acct_num)+','+str(self.type)+','+str(self.value)

    def toString(self):
        return str(self.date)+','+str(self.acct_num)+','+str(self.type)+','+str(self.value)

if __name__ == '__main__':
    print('transaction.py...')