import datetime
import os

class TransactionModel:
    _TRANSACTION_COLUMNS = 'date,uid,account_type,account_number,transaction_type,amount'

    def __init__(self):
        pass

    def open_transaction_file(self):
        pass

    def create_new_entry(self, uid, account_type, account_num, transaction_type, amount, date=datetime.datetime.now()):
        row = '{0},{1},{2},{3},{4},{5}'.format(str(date), uid, account_type, account_num, transaction_type, str(float(amount)), )
        self.save_transaction(uid, row)

    # To be used with CLI only
    def delete_from_file(self, uid):
        pass

    # To be used with CLI only
    def edit_entry(self, uid, type, amount):
        pass

    def save_transaction(self, uid, row):
        filename = 'model/logs/'+str(uid)+'-transactions.csv'
        try:
            if os.path.getsize(filename) > 0:
                with open(filename, 'a') as csv_file:
                    csv_file.write('\n'+row)
            else:
                with open(filename, 'w') as csv_file:
                    output = self._TRANSACTION_COLUMNS + '\n' + row
                    csv_file.write(output)
        except OSError:
            with open(filename, 'w') as csv_file:
                output = self._TRANSACTION_COLUMNS + '\n' + row
                csv_file.write(output)


if __name__ == '__main__':
    pass
