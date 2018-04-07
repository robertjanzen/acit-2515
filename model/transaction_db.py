import csv
import datetime

class TransactionDB:
    _DB_COLUMNS = ['date', 'uid', 'type', 'amount']

    def __init__(self, db_file):
        self._db_file = db_file
        self._db_content = []

        self.open_db_file()

    @property
    def db_content(self):
        return self._db_content

    def open_db_file(self):
        pass

    def create_new_entry(self, uid, type, amount, date=datetime.datetime.now()):
        pass

    # To be used with CLI only
    def delete_from_file(self, input_uid):
        pass

    # To be used with CLI only
    def edit_entry(self, input_uid, input_type, input_value):
        pass

    def save_to_file(self):
        pass

if __name__ == '__main__':
    pass
