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
        
        self.usr_acc_dic = None
        self.usr_target_acc = None
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

            if input_cmd == 'Back':
                # check for if we went from Done to Selection by clicking NO
                if self.state_db.prev_state == 'Done':
                    self.state_db.state = 'Selection'
                else:
                    self.state_db.state = self.state_db.prev_state

            elif input_cmd == 'Other':
                if self.state_db.state == 'Selection':
                    self.selection_page_num += 1
                    self.state_db.state = 'Selection'

            elif input_cmd == 'DEL':
                if self.state_db.state == 'Deposit':
                    last_index = len(self.view.mid_title_input.get()) - 1
                    self.view.mid_title_input.delete(last_index)

            elif input_cmd == 'OK':
                if self.state_db.state == 'Deposit':
                    entry = self.view.mid_title_input.get()
                    
                    print("You deposited: $%s" % entry)
                    self.state_db.state = 'Done'

            elif input_cmd == '':
                return

            else:
                if self.state_db.state == 'Selection':
                    
                    offset = int(input_cmd[0]) - 1
        
                    target_acc_num = list(self.usr_acc_dic.keys())[self.selection_page_num * 4 + offset]
                    for item in self.account_db:
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
                    print('Withdrawing....')
                    self.state_db.state = 'Done'
    
                elif self.state_db.state == 'Done':
                    if input_cmd == 'Yes':
                        self.state_db.state = 'Card'
    
                    elif input_cmd == 'No':
                        self.state_db.state = 'Overview'
            
            
            
            # if self.state_db.state == 'Selection':
            #
            #     elif input_cmd == 'Other':
            #         self.selection_page_num += 1
            #         self.state_db.state = 'Selection'
            #
            #     elif input_cmd != 'OK' and input_cmd != 'DEL':
            #         if input_cmd != '':
            #             offset = int(input_cmd[0]) - 1
            #
            #             target_acc_num = list(self.usr_acc_dic.keys())[self.selection_page_num * 4 + offset]
            #             for item in self.account_db:
            #                 if item['acc_num'] == target_acc_num:
            #                     self.usr_target_acc = item
            #                     break
            #
            #             self.state_db.state = "Overview"
            #
            # elif self.state_db.state == 'Overview':
            #     if input_cmd == 'Balance':
            #         self.state_db.state = 'Balance'
            #
            #     elif input_cmd == 'Deposit':
            #         self.state_db.state = 'Deposit'
            #
            #     elif input_cmd == 'Withdraw':
            #         self.state_db.state = 'Withdraw'
            #
            #     # elif input_cmd == 'Back':
            #     #     self.state_db.state = 'Selection'
            #
            # elif self.state_db.state == 'Balance':
            #     # if input_cmd == 'Back':
            #     #     self.state_db.state = 'Overview'
            #     pass
            #
            # elif self.state_db.state == 'Deposit':
            #     if input_cmd == 'OK':
            #         pass
            #
            #     elif input_cmd == 'DEL':
            #         pass
            #
            #     # elif input_cmd == 'Back':
            #     #     self.state_db.state = 'Overview'
            #
            # elif self.state_db.state == 'Withdraw':
            #     if input_cmd == '20':
            #         pass
            #
            #     elif input_cmd == '500':
            #         pass
            #
            #     elif input_cmd == '100':
            #         pass
            #
            #     elif input_cmd == 'Other':
            #         pass
            #
            #     # elif input_cmd == 'Back':
            #     #     self.state_db.state = 'Overview'
            #
            # elif self.state_db.state == 'Done':
            #     if input_cmd == 'Yes':
            #         self.state_db.state = 'Card'
            #
            #     elif input_cmd == 'No':
            #         self.state_db.state = 'Overview'

        elif 'state' in updated_data:
            new_state = kwargs['state']
            
            if new_state == 'Selection':
                self.usr_target_acc = {}
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
                
            elif new_state == 'Done':
                self.view.render_done()
            
            elif new_state == 'Card':
                self.clear_controller_data()

    def get_account_list(self):
        
        for entry in self.account_db:
            if entry['uid'] == self.state_db.uid:
                self.usr_acc_dic[entry['acc_num']] = entry['acc_name']
                
    def clear_controller_data(self):
        self.usr_target_acc = None
        self.usr_acc_dic = None
        self.selection_page_num = -1
                

if __name__ == '__main__':
    print('Transaction Controller')