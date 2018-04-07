from tkinter import *
from observe.observer import Observer
from datetime import datetime
from datetime import timedelta

class TransactionController(Observer):

    def __init__(self, view, state_model, account_db):
        self.view = view
        self.state_db = state_model
        self.state_db.add_observer(self)
        self.account_db = account_db

    def update(self, publisher, **kwargs):
        updated_data = kwargs.keys()

        if 'entry' in updated_data:
            pass

        elif 'input' in updated_data:
            pass

        elif 'state' in updated_data:
            new_state = kwargs['state']
            if new_state == 'deposit':
                pass
            elif new_state == 'overview':
                pass
            elif new_state == 'withdraw':
                pass
            elif new_state == 'done':
                pass
            elif new_state == 'info':
                pass

if __name__ == '__main__':
    print('Transaction Controller')