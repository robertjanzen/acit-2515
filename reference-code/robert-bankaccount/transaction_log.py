# transaction_log.py
#
# Bank account program
#
# Robert Janzen A01029341 2B

from transaction import Transaction

class TransactionLog():

    def __init__(self, account_number, transactions=[]):
        self.account_number = account_number
        self.session_transactions = transactions

    def save(self, type, value, acct_num):
        new_transaction = Transaction(type, value, self.account_number)
        self.session_transactions.append(new_transaction)

        f = open(str(self.account_number)+'-transactions.txt', 'a+')
        f.write(new_transaction.toString()+'\n')
        f.close()
        return

    def list_from_file(self):
        f = open(str(self.account_number)+'-transactions.txt', 'r')
        for line in [line.rstrip() for line in f.readlines()]:
            print(line)
        return

    def list_session_transactions(self):
        for item in self.session_transactions:
            print(item)
        return

if __name__ == '__main__':
    print('transaction_log.py...')