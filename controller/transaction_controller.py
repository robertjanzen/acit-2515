from tkinter import *
from observe.observer import Observer
from datetime import datetime
from datetime import timedelta

class TransactionController(Observer):

    def __init__(self, view, state_model, user_db):
        self.view = view
        self.state_db = state_model
        self.state_db.add_observer(self)
        self.db = user_db

if __name__ == '__main__':
    print('Transaction Controller')