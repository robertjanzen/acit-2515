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
        self.state_model = state_model
        self.state_model.addObserver(self)
        self.account_model = account_model
        self.transaction_model = trans_model
        self.current_total = 0.0
        self.user_accounts = None
        self.selected_account_info = None
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

            if self.state_model.state in ['Deposit', 'Cash']:
                new_digit = float(input_value) * 0.01
                self.current_total *= 10.0
                self.current_total = round((self.current_total + new_digit), 2)
                self.view.mid_title_input.delete(0, END)
                self.view.mid_title_input.insert(END, '{0:.2f}'.format(self.current_total))

        elif 'input' in updated_data:
            input_command = kwargs['input']

            if input_command == 'Back':

                prev_state = self.state_model.prev_state
                self.current_total = 0.0
                self.state_model.state = prev_state

            elif input_command == 'Other':
                if self.state_model.state == 'Selection':
                    self.selection_page_num += 1
                    self.state_model.state = 'Selection'
                elif self.state_model.state == 'Withdraw':
                    self.state_model.state = 'Cash'

            elif input_command == 'DEL':
                if self.state_model.state in ['Deposit', 'Cash']:
                    self.current_total = 0.00
                    self.view.mid_title_input.delete(0, END)
                    self.view.mid_title_input.insert(END, '{0:.2f}'.format(self.current_total))

            elif input_command == 'OK':

                entry = self.view.mid_title_input.get()
                if entry == '':
                    return

                if self.state_model.state == 'Deposit':
                    self.current_total = 0.0
                    try:
                        dollar_amt = float(entry)
                        converted = True
                    except:
                        converted = False

                    if converted:
                        self.deposit(entry)
                        
                        if self.selected_account_info is None:
                            self.state_model.state = 'Error'
                        else:
                            self.info_msg = dollar_amt
                            self.state_model.state = 'DConfirm'

                elif self.state_model.state == 'Cash':
                    try:
                        dollar_amt = float(entry)
                        converted = True
                    except:
                        converted = False
                        
                    if converted:
                        withdrawal_result = self.withdraw(entry)
                        
                        if withdrawal_result != '':
                            self.error_msg = withdrawal_result
                            self.state_model.state = 'Error'
                        else:
                            self.info_msg = entry
                            self.state_model.state = 'WConfirm'
            
            elif input_command == 'Continue':
                if self.state_model.state in ['WConfirm', 'DConfirm']:
                    self.state_model.state = 'Done'

            elif input_command == '':
                return

            else:
                if self.state_model.state == 'Selection':

                    offset = int(input_command[0]) - 1

                    target_acc_num = list(self.user_accounts.keys())[self.selection_page_num * 4 + offset]
                    self.updateTargetAccountInfo(self.state_model.uid, target_acc_num)
                    
                    if self.selected_account_info is None:
                        self.state_model.state = 'Error'
                    else:
                        self.selection_page_num = -1
                        self.state_model.state = 'Overview'

                elif self.state_model.state == 'Overview':
                    if input_command == 'Balance':
                        self.state_model.state = 'Balance'

                    elif input_command == 'Deposit':
                        self.state_model.state = 'Deposit'

                    elif input_command == 'Withdraw':
                        self.state_model.state = 'Withdraw'

                elif self.state_model.state == 'Withdraw':
                    amount = input_command.strip('$')
                    
                    result = self.withdraw(amount)
                    if result != '':
                        self.error_msg = result
                        self.state_model.state = 'Error'
                        
                    else:
                        self.info_msg = amount
                        self.state_model.state = 'WConfirm'

                elif self.state_model.state == 'Done':
                    if input_command == 'Yes':
                        self.state_model.state = 'Card'

                    elif input_command == 'No':
                        self.state_model.state = 'Overview'

        elif 'state' in updated_data:
            new_state = kwargs['state']
            
            if new_state == 'Selection':
                self.selected_account_info = {}
                self.user_accounts = {}
                self.getAccountList()
                
                if self.selection_page_num != -1:
                    options = []
                    acc_pool = list(self.user_accounts.keys())

                    if self.selection_page_num >= math.ceil(len(acc_pool) / 4):
                        self.selection_page_num = 0

                    start_index = self.selection_page_num * 4

                    for x in range(4):
                        if start_index + x < len(acc_pool):
                            options.append(str(x + 1) + '-' + self.user_accounts[acc_pool[start_index + x]])
                        else:
                            options.append('')

                    self.view.renderSelection(options[0], options[1], options[2], options[3], 'Other')

                else:
                    self.selection_page_num = 0
                    self.state_model.state = "Selection"

            elif new_state == 'Overview':
                self.updateTargetAccountInfo(self.state_model.uid, self.selected_account_info['acc_num'])
                if self.selected_account_info is None:
                    self.view.renderError("Account Not Found")
                else:
                    self.view.renderOverview('', '', '')

            elif new_state == 'Balance':
                self.updateTargetAccountInfo(self.state_model.uid, self.selected_account_info['acc_num'])
                if self.selected_account_info is None:
                    self.view.renderError("Account Not Found")
                else:
                    self.view.renderBalance('Your Current Balance:', '${}'.format(self.selected_account_info['acc_balance']),
                                         'Cancel', 'Back')

            elif new_state == 'Deposit':
                self.view.renderDeposit()

            elif new_state == 'Withdraw':
                self.view.renderWithdraw()

            elif new_state == 'Cash':
                self.view.renderCash()

            elif new_state == 'Done':
                self.view.renderDone()

            elif new_state == 'Card':
                self.clearControllerData()
                
            elif new_state == 'Error':
                self.view.renderError(self.error_msg)
            
            elif new_state == 'WConfirm':
                self.view.renderWithdrawalConfirmation(self.info_msg)
            
            elif new_state == 'DConfirm':
                self.view.renderDepositConfirmation(self.info_msg)

    def updateTargetAccountInfo(self, uid, acc_num):
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
                self.selected_account_info = entry
                
                return
        
        self.selected_account_info = None

    def getAccountList(self):
        """
            Get a list of accounts tied to the currently signed in user uid.
            
        Returns:
            None
        """

        for entry in self.account_model.accounts:
            
            if entry['uid'] == self.state_model.uid:
                self.user_accounts[entry['acc_num']] = entry['acc_name']

    def clearControllerData(self):
        """
            Clears controller user session data
            
        Returns:
            None
        """
        
        self.selected_account_info = None
        self.user_accounts = None
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
        
        uid = self.state_model.uid

        account_num = self.selected_account_info['acc_num']
        account_type = self.selected_account_info['acc_type']

        self.updateTargetAccountInfo(uid, account_num)
        if self.selected_account_info is None:
            self.error_msg = 'Account Not Found'
            return

        # Step 1 update balance in user's database file
        self.account_model.deposit(uid, account_num, amount)

        # Step 2 save transaction to file
        self.transaction_model.createNewEntry(uid, account_type, account_num, 'Deposit', amount)

    def withdraw(self, input_value):
        """
            Withdraw money from the account
            
        Args:
            input_value:
                The amount to be withdrawn from the account
                
        Returns:
            String containing the result of the withdraw attempt
        """
        
        uid = self.state_model.uid
        
        account_num = self.selected_account_info['acc_num']
        account_type = self.selected_account_info['acc_type']
        
        self.updateTargetAccountInfo(uid, account_num)
        
        if self.selected_account_info is None:
            return 'Account Not Found'
        
        else:
        
            transaction_result = self.account_model.withdraw(uid, account_num, input_value)
            
            if transaction_result == '':
                self.transaction_model.createNewEntry(uid, account_type, account_num, 'Withdraw', input_value)
            
            return transaction_result
    

if __name__ == '__main__':
    print('Transaction Controller')
