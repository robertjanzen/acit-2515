# transaction.py
#
# ATM MVC program
#
# Team alroda
#
# Aldrich Huang A01026502 2B
# Robert Janzen A01029341 2B
# David Xiao A00725026 2B

from tkinter import *
from observe.observer import Observer
import math

class TransactionController(Observer):

    def __init__(self, view, state_model, account_model, trans_model):
        self.view = view
        self.state_db = state_model
        self.state_db.add_observer(self)
        self.account_model = account_model
        self.transaction_model = trans_model
        self.current_total = 0.0
        self.usr_acc_dic = None
        self.usr_target_acc = None
        self.selection_page_num = -1
        self.info_msg = ''
        self.error_msg = ''

    def update(self, publisher, **kwargs):
        """
            Update the ATM view depending on the state and updated input
        Args:
            publisher:
                Object that's updated
            **kwargs:
                Updated attribute name and value as reported by the observer
                
        Returns:
            None
        """
        
        updated_data = kwargs.keys()

        if 'entry' in updated_data:
            input_value = kwargs['entry']

            if self.state_db.state in ['Deposit', 'Cash']:
                new_digit = float(input_value) * 0.01
                self.current_total *= 10.0
                self.current_total = round((self.current_total + new_digit), 2)
                self.view.mid_title_input.delete(0, END)
                self.view.mid_title_input.insert(END, '{0:.2f}'.format(self.current_total))

        elif 'input' in updated_data:
            input_cmd = kwargs['input']

            if input_cmd == 'Back':

                prev_state = self.state_db.prev_state
                self.current_total = 0.0
                self.state_db.state = prev_state

            elif input_cmd == 'Other':
                if self.state_db.state == 'Selection':
                    self.selection_page_num += 1
                    self.state_db.state = 'Selection'
                elif self.state_db.state == 'Withdraw':
                    self.state_db.state = 'Cash'

            elif input_cmd == 'DEL':
                if self.state_db.state in ['Deposit', 'Cash']:
                    self.current_total = 0.00
                    self.view.mid_title_input.delete(0, END)
                    self.view.mid_title_input.insert(END, '{0:.2f}'.format(self.current_total))

            elif input_cmd == 'OK':

                entry = self.view.mid_title_input.get()
                if entry == '':
                    return

                if self.state_db.state == 'Deposit':
                    self.current_total = 0.0
                    try:
                        dollar_amt = float(entry)
                        converted = True
                    except:
                        converted = False

                    if converted:
                        self.deposit(entry)
                        
                        if self.usr_target_acc is None:
                            self.state_db.state = 'Error'
                        else:
                            self.state_db.state = 'Done'

                elif self.state_db.state == 'Cash':

                    # Should probably check to see if account has enough balance
                    try:
                        dollar_amt = float(entry)
                        converted = True
                        
                    except:
                        converted = False
                        
                    if converted:
                        
                        withdrawal_result = self.withdraw(entry)
                        
                        if withdrawal_result != '':
                            self.error_msg = withdrawal_result
                            self.state_db.state = 'Error'
                        
                        else:
                            self.info_msg = entry
                            self.state_db.state = 'Confirm'
            
            elif input_cmd == 'Continue':
                if self.state_db.state == 'Confirm':
                    self.state_db.state = 'Done'

            elif input_cmd == '':
                return

            else:
                if self.state_db.state == 'Selection':

                    offset = int(input_cmd[0]) - 1

                    target_acc_num = list(self.usr_acc_dic.keys())[self.selection_page_num * 4 + offset]
                    self.update_tgt_acc_info(self.state_db.uid, target_acc_num)
                    
                    if self.usr_target_acc is None:
                        self.state_db.state = 'Error'
                    else:
                        self.selection_page_num = -1
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
                    
                    result = self.withdraw(amount)
                    if result != '':
                        self.error_msg = result
                        self.state_db.state = 'Error'
                        
                    else:
                        self.info_msg = amount
                        self.state_db.state = 'Confirm'

                elif self.state_db.state == 'Done':
                    if input_cmd == 'Yes':
                        self.state_db.state = 'Card'

                    elif input_cmd == 'No':
                        self.state_db.state = 'Overview'

        elif 'state' in updated_data:
            new_state = kwargs['state']
            
            if new_state == 'Selection':
                self.usr_target_acc = {}
                self.usr_acc_dic = {}
                self.get_account_list()
                
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
                    self.state_db.state = "Selection"

            elif new_state == 'Overview':
                self.update_tgt_acc_info(self.state_db.uid, self.usr_target_acc['acc_num'])
                if self.usr_target_acc is None:
                    self.view.render_error("Account Not Found")
                else:
                    self.view.render_overview('', '', '')

            elif new_state == 'Balance':
                self.update_tgt_acc_info(self.state_db.uid, self.usr_target_acc['acc_num'])
                if self.usr_target_acc is None:
                    self.view.render_error("Account Not Found")
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
                
            elif new_state == 'Error':
                self.view.render_error(self.error_msg)
            
            elif new_state == 'Confirm':
                self.view.render_withdrawal_confirmation(self.info_msg)

    def update_tgt_acc_info(self, uid, acc_num):
        """
            Reloads the selected account's information
            
        Args:
            uid:
                UID of the user who owns the account
            acc_num:
                Account number of the account
                
        Returns:
            None
        """
        
        for entry in self.account_model.accounts:
            if entry['uid'] == uid and entry['acc_num'] == acc_num:
                self.usr_target_acc = entry
                
                return
        
        self.usr_target_acc = None

    def get_account_list(self):
        """
            Get a list of accounts tied to the currently signed in user uid.
            
        Returns:
            None
        """

        for entry in self.account_model.accounts:
            
            if entry['uid'] == self.state_db.uid:
                self.usr_acc_dic[entry['acc_num']] = entry['acc_name']

    def clear_controller_data(self):
        """
            Clears controller user session data
            
        Returns:
            None
        """
        
        self.usr_target_acc = None
        self.usr_acc_dic = None
        self.selection_page_num = -1
        self.info_msg = ''
        self.error_msg = ''

    def deposit(self, amount):
        """
            Deposits money into the selected account
            
        Args:
            amount:
                The amount to be deposited to the account
                
        Returns:
            None
        """
        
        uid = self.state_db.uid

        account_num = self.usr_target_acc['acc_num']
        account_type = self.usr_target_acc['acc_type']

        self.update_tgt_acc_info(uid, account_num)
        if self.usr_target_acc is None:
            self.error_msg = 'Account Not Found'
            return

        # Step 1 update balance in user's database file
        self.account_model.deposit(uid, account_num, amount)

        # Step 2 save transaction to file
        self.transaction_model.create_new_entry(uid, account_type, account_num, 'Deposit', amount)

    def withdraw(self, input_value):
        """
            Withdraw money from the account
            
        Args:
            input_value:
                The amount to be withdrawn from the account
                
        Returns:
            String containing the result of the withdraw attempt
        """
        
        uid = self.state_db.uid
        
        account_num = self.usr_target_acc['acc_num']
        account_type = self.usr_target_acc['acc_type']
        
        self.update_tgt_acc_info(uid, account_num)
        
        if self.usr_target_acc is None:
            return 'Account Not Found'
        
        else:
        
            transaction_result = self.account_model.withdraw(uid, account_num, input_value)
            
            if transaction_result == '':
                self.transaction_model.create_new_entry(uid, account_type, account_num, 'Withdraw', input_value)
            
            return transaction_result
    

if __name__ == '__main__':
    print('Transaction Controller')
