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

    def deposit(self):
        pass

    def withdraw(self):
        pass

    def update(self, publisher, **kwargs):
        updated_data = kwargs.keys()

        if 'entry' in updated_data:
            pass

        elif 'input' in updated_data:
            input_cmd = kwargs['input']
            if self.state_db.state == 'Selection':
                if input_cmd == 'Chequing':
                    self.state_db.state = 'Overview'
                elif input_cmd == 'Savings':
                    self.state_db.state = 'Overview'
                elif input_cmd == 'Other':
                    self.state_db.state = 'Overview'

            elif self.state_db.state == 'Overview':
                if input_cmd == 'Balance':
                    self.state_db.state = 'Balance'
                elif input_cmd == 'Deposit':
                    self.state_db.state = 'Deposit'
                elif input_cmd == 'Withdraw':
                    self.state_db.state = 'Withdraw'

            elif self.state_db.state == 'Balance':
                if input_cmd == 'Back':
                    self.state_db.state = 'Overview'

            elif self.state_db.state == 'Deposit':
                if input_cmd == 'OK':
                    pass
                elif input_cmd == 'DEL':
                    pass
                elif input_cmd == 'Back':
                    self.state_db.state = 'Overview'

            elif self.state_db.state == 'Withdraw':
                if input_cmd == '20':
                    pass
                elif input_cmd == '500':
                    pass
                elif input_cmd == '100':
                    pass
                elif input_cmd == 'Other':
                    pass
                elif input_cmd == 'Back':
                    self.state_db.state = 'Overview'

            elif self.state_db.state == 'Done':
                if input_cmd == 'Yes':
                    self.state_db.state = 'Card'
                elif input_cmd == 'No':
                    self.state_db.state = 'Overview'

        elif 'state' in updated_data:
            new_state = kwargs['state']
            if new_state == 'Selection':
                self.view.render_selection('Chequing','Savings','','','Other')
            elif new_state == 'Overview':
                self.view.render_overview('1','1','1')
            elif new_state == 'Balance':
                self.view.render_balance('a','b','Cancel','Back')
            elif new_state == 'Deposit':
                self.view.render_deposit()
            elif new_state == 'Withdraw':
                self.view.render_withdraw()
            elif new_state == 'Done':
                self.view.render_done()

if __name__ == '__main__':
    print('Transaction Controller')