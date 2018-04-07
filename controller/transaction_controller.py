from tkinter import *
from observe.observer import Observer
from datetime import datetime
from datetime import timedelta

import math

class TransactionController(Observer):

    def __init__(self, view, state_model, account_db):
        self.view = view
        self.state_db = state_model
        self.state_db.add_observer(self)
        self.account_db = account_db
        
        self.usr_acc_dic = {}
        self.usr_target_acc = {}
        self.selection_page_num = -1

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
                    self.selection_page_num += 1
                    self.state_db.state = 'Selection'

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
                
                if self.selection_page_num != -1:
                    options = []
                    acc_pool = list(self.usr_acc_dic.keys())
                    
                    if self.selection_page_num >= math.floor(len(acc_pool) % 4):
                        self.selection_page_num = 0
                    
                    start_index = self.selection_page_num * 4
                    
                    for x in range(4):
                        if start_index + x < len(acc_pool):
                            options.append(str(x + 1) + '-' + self.usr_acc_dic[acc_pool[start_index + x]])
                        else:
                            options.append('')
                    
                    self.view.render_selection(options[0], options[1], options[2], options[3], 'Other')
                    
                else:
                    self.selection_page_num = 0
                    self.get_account_list()
                    self.state_db.state = "Selection"
                
            elif new_state == 'Overview':
                self.view.render_overview('', '', '')
                
            elif new_state == 'Balance':
                self.view.render_balance('Your Current Balance:', '$', 'Cancel', 'Back')
                
            elif new_state == 'Deposit':
                self.view.render_deposit()
                
            elif new_state == 'Withdraw':
                self.view.render_withdraw()
                
            elif new_state == 'Done':
                self.view.render_done()

    def get_account_list(self):
        
        for entry in self.account_db:
            if entry['uid'] == self.state_db.uid:
                self.usr_acc_dic[entry['acc_num']] = entry['acc_name']
                

if __name__ == '__main__':
    print('Transaction Controller')