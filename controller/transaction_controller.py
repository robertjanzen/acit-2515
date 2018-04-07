from tkinter import *
from observe.observer import Observer
from datetime import datetime
from datetime import timedelta

import math

class TransactionController(Observer):

    def __init__(self, view, state_model, account_model, trans_model):
        self.view = view
        self.state_db = state_model
        self.state_db.add_observer(self)
        self.account_model = account_model
        self.transaction_model = trans_model
        
        self.usr_acc_dic = None
        self.usr_target_acc = None
        self.selection_page_num = -1

    def update(self, publisher, **kwargs):
        updated_data = kwargs.keys()

        if 'entry' in updated_data:
            input_value = kwargs['entry']
            
            if self.state_db.state in ['Deposit', 'Cash']:
                self.view.mid_title_input.insert(END, input_value)

        elif 'input' in updated_data:
            input_cmd = kwargs['input']

            if input_cmd == 'Back':

                prev_state = self.state_db.prev_state
                
                self.state_db.state = prev_state

            elif input_cmd == 'Other':
                if self.state_db.state == 'Selection':
                    self.selection_page_num += 1
                    self.state_db.state = 'Selection'
                elif self.state_db.state == 'Withdraw':
                    self.state_db.state = 'Cash'

            elif input_cmd == 'DEL':
                if self.state_db.state in ['Deposit', 'Cash']:
                    last_index = len(self.view.mid_title_input.get()) - 1
                    self.view.mid_title_input.delete(last_index)

            elif input_cmd == 'OK':
    
                entry = self.view.mid_title_input.get()
                if entry == '':
                    return
                
                if self.state_db.state == 'Deposit':
                    
                    # Update account balance and stuff
                    
                    
                    try:
                        dollar_amt = float(entry)
                        converted = True
                    except:
                        converted = False
                        
                    if converted:
                        # self.deposit(dollar_amt)
                        print("Depositing $%s..." % dollar_amt)
                        self.state_db.state = 'Done'
                    
                elif self.state_db.state == 'Cash':
                    
                    # Should probably check to see if account has enough balance
                    self.withdraw(float(entry))

            elif input_cmd == '':
                return

            else:
                if self.state_db.state == 'Selection':
                    
                    offset = int(input_cmd[0]) - 1
        
                    target_acc_num = list(self.usr_acc_dic.keys())[self.selection_page_num * 4 + offset]
                    for item in self.account_model:
                        if item['acc_num'] == target_acc_num:
                            self.usr_target_acc = item
                            break
                    
                    self.state_db.state = 'Overview'
    
                elif self.state_db.state == 'Overview':
                    if input_cmd == 'Balance':
                        self.state_db.state = 'Balance'
        
                    elif input_cmd == 'Deposit':
                        self.state_db.state = 'Deposit'
        
                    elif input_cmd == 'Withdraw':
                        self.state_db.state = 'Withdraw'
    
                elif self.state_db.state == 'Withdraw':
                    amount = input_cmd.strip('$')
                    self.withdraw(amount)
                    
                    self.state_db.state = 'Done'
    
                elif self.state_db.state == 'Done':
                    if input_cmd == 'Yes':
                        self.state_db.state = 'Card'
    
                    elif input_cmd == 'No':
                        self.state_db.state = 'Overview'

        elif 'state' in updated_data:
            new_state = kwargs['state']
            
            if new_state == 'Selection':
                self.usr_target_acc = {}
                if self.selection_page_num != -1:
                    options = []
                    acc_pool = list(self.usr_acc_dic.keys())
                    
                    if self.selection_page_num >= math.ceil(len(acc_pool) / 4):
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
                    self.usr_acc_dic = {}
                    self.get_account_list()
                    self.state_db.state = "Selection"
                
            elif new_state == 'Overview':
                self.view.render_overview('', '', '')
                
            elif new_state == 'Balance':
                self.view.render_balance('Your Current Balance:', '${}'.format(self.usr_target_acc['acc_balance']),
                                         'Cancel', 'Back')
                
            elif new_state == 'Deposit':
                self.view.render_deposit()
                
            elif new_state == 'Withdraw':
                self.view.render_withdraw()
            
            elif new_state == 'Cash':
                self.view.render_cash()
                
            elif new_state == 'Done':
                self.view.render_done()
            
            elif new_state == 'Card':
                self.clear_controller_data()

    def get_account_list(self):
        for entry in self.account_model.accounts:
            if entry['uid'] == self.state_db.uid:
                self.usr_acc_dic[entry['acc_num']] = entry['acc_name']
                
    def clear_controller_data(self):
        self.usr_target_acc = None
        self.usr_acc_dic = None
        self.selection_page_num = -1

    def deposit(self, amount):
        uid = self.account_model['uid']
        account_type = self.account_model['type']

        # Step 1 save transaction to file
        self.transaction_model.create_new_entry(uid, account_type, 'Deposit', amount)

        # Step 2 update balance in user's database file

    def withdraw(self, input_value):
        dollar_value = float(input_value)
        
        # Do Withdraw logic here...
        print("Withdrawing $%.2f..." % dollar_value)
        self.state_db.state = 'Done'


if __name__ == '__main__':
    print('Transaction Controller')