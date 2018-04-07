import csv
import datetime

class TransactionModel:
    _TRANSACTION_COLUMNS = ['date', 'uid', 'account', 'type', 'amount']

    def __init__(self):
        self._transaction_file = ''
        self._transaction_content = []

    @property
    def transaction_content(self):
        return self._transaction_content

    def open_transaction_file(self):
        pass

    def create_new_entry(self, uid, type, amount, date=datetime.datetime.now()):
        pass

    # To be used with CLI only
    def delete_from_file(self, uid):
        pass

    # To be used with CLI only
    def edit_entry(self, uid, type, amount):
        pass

    def save_to_file(self, uid, account_type, transaction_type, amount):
        filename = uid+'transactions.txt'
        with open(filename, 'a', newline='') as csv_file:
            fields = self._TRANSACTION_COLUMNS
            writer = csv.DictWriter(csv_file, fieldnames=fields)

            for entry in self.transaction_content:
                writer.writerow(entry)

if __name__ == '__main__':
    pass
