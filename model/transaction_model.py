import csv
import datetime

class TransactionModel:
    _TRANSACTION_COLUMNS = ['date', 'uid', 'account', 'type', 'amount']

    def __init__(self):
        pass

    def open_transaction_file(self):
        pass

    def create_new_entry(self, uid, account_type, transaction_type, amount, date=datetime.datetime.now()):
        row = str(date) + ',' + uid + ',' + account_type + ',' + transaction_type + ',' + str(amount)
        self.save_transaction(uid, row)

    # To be used with CLI only
    def delete_from_file(self, uid):
        pass

    # To be used with CLI only
    def edit_entry(self, uid, type, amount):
        pass

    def save_transaction(self, uid, row):
        filename = uid+'transactions.csv'
        with open(filename, 'a', newline='') as csv_file:
            fields = self._TRANSACTION_COLUMNS
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writerow(row)

if __name__ == '__main__':
    pass
