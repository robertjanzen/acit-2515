# account_model.py
#
# ATM MVC program
#
# Team alroda
#
# Aldrich Huang A01026502 2B
# Robert Janzen A01029341 2B
# David Xiao A00725026 2B

import json

class AccountModel:

    _NEXT_ACC_NUMBER = ''
    _NEXT_UID = ''
    _OVERDRAFT_LIMIT = -500

    def __init__(self):
        self._accounts = None
        self.loadAccount()

    @property
    def accounts(self):
        self.loadAccount()
        return self._accounts

    @accounts.setter
    def accounts(self, input_value):
        self._accounts = input_value

    def loadAccount(self):
        """
            Load user all user accounts from the account_db JSON file into a list of objects

        Returns:
            None

        """
        with open('model/account_model.json') as json_file:
            self.accounts = json.load(json_file)
        with open('model/next_account_number.txt') as num_file:
            AccountModel._NEXT_UID = int(num_file.readline())
            AccountModel._NEXT_ACC_NUMBER = int(num_file.readline())

    def createNewAccount(self, acc_type, acc_name, acc_balance=0, uid = '', acc_num = ''):
        """
            Create a new chequing or savings account for an existing user, then request that the new account be
            saved to file.

        Args:
            acc_type:
                The type of account, can be chequing or savings
            acc_name:
                A descriptive name for the account like Vacation Fund, or Education Savings
            acc_balance:
                A starting balance for the account if money is being deposited right away
            uid:
                The user ID of the user creating the account
            acc_num:
                An auto generated account number

        Returns:
            The UID which the account was created for

        """
        if uid == '':
            uid = str(AccountModel._NEXT_UID)
            AccountModel._NEXT_UID += 1
        if acc_num == '':
            acc_num = str(AccountModel._NEXT_ACC_NUMBER)
            AccountModel._NEXT_ACC_NUMBER += 1
        user_object = {
            "uid": uid,
            "acc_num": acc_num,
            "acc_type": acc_type,
            "acc_name": acc_name,
            "acc_balance": acc_balance
        }
        self.saveAccountToFile(user_object)
        return acc_num

    def saveAccountToFile(self, user_object):
        """
            Using an object which contains the user's account information, save the data into a json file in local
            storage

        Args:
            user_object:
                A python object containing the uid, account number, account type, and account balance
        Returns:
            None

        """
        exists = False
        with open('model/next_account_number.txt','w') as num_file:
            next_data = str(AccountModel._NEXT_UID)+'\n'+str(AccountModel._NEXT_ACC_NUMBER)
            num_file.write(next_data)
        with open('model/account_model.json') as json_file:
            data = json.load(json_file)
            for account in data:
                if (account['uid'] == user_object['uid']) and (account['acc_num'] == user_object['acc_num']):
                    exists = True
            if not exists:
                data.append(user_object)
            else:
                print('Account already exists')

        with open('model/account_model.json', 'w') as out_file:
            json.dump(data, out_file, indent=4)
        return

    def deleteAccount(self, uid, acc_num):
        """
            Delete a user's account by providing their UID and a specific account number

        Args:
            uid:
                The user ID which owns the account being deleted
            acc_num:
                The account number for the account being deleted
        Returns:
            Returns True if the account was deleted successfully, and False otherwise
        """
        with open('model/account_model.json', 'r') as json_file:
            data = json.load(json_file)
        for index, account in enumerate(data):
            if (account['uid'] == uid) and (account['acc_num'] == acc_num):
                if float(data[index]['acc_balance']) != 0.0:
                    return False
                else:
                    data.remove(account)
        with open('model/account_model.json', 'w') as json_file2:
            json_file2.seek(0)
            json.dump(data, json_file2, indent=4)
        return True

    def changeName(self, uid, acc_num, account_name):
        """
            Change the name of a bank account. For example change an account called "Vacation Fund" to "Wedding Fund"

        Args:
            uid:
                The user ID which owns that account being renamed
            acc_num:
                The account number for the account which is being renamed
            account_name:
                The new account name

        Returns:
            Returns True if the account name was successfully update, and False otherwise

        """
        with open('model/account_model.json', 'r+') as json_file:
            data = json.load(json_file)
            for index, account in enumerate(data):
                if (account['uid'] == uid) and (account['acc_num'] == acc_num):
                    data[index]['acc_name'] = str(account_name)
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
        return True

    def withdraw(self, uid, account_num, amount):
        """
            Withdraw money from an account is there is sufficient funds, otherwise return an error message

        Args:
            uid:
                The user ID of the account which is attempting to withdraw funds
            account_num:
                The account number for which funds are being withdrawn from
            amount:
                The requested amount to be withdrawn

        Returns:
            Empty string if the withdrawal was a success, and an error message if there were insufficient funds, they
            exceeded their overdraft limit, an unknown account type was used, or invalid input was given

        """
        return_msg = ''

        if self.checkFloat(amount):

            with open('model/account_model.json') as json_file:

                data = json.load(json_file)

            for index, account in enumerate(data):
                
                if (account['uid'] == uid) and (account['acc_num'] == account_num):
                    
                    new_amount = round(float(data[index]['acc_balance']) - float(amount), 2)
                    
                    if account['acc_type'] == 'Chequing':
                        if new_amount >= self._OVERDRAFT_LIMIT:
                            data[index]['acc_balance'] = str(new_amount)
                            break
                        else:
                            return_msg = 'Exceeded Overdraft Limit'
                            
                    elif account['acc_type'] == 'Savings':
                        if new_amount >= 0:
                            data[index]['acc_balance'] = str(new_amount)
                            break
                        else:
                            return_msg = 'Insufficient Funds'
                    
                    else:
                        return_msg = 'Unknown Account Type'
                        
            if return_msg == '':
                with open('model/account_model.json', 'w') as json_file2:
                    
                    json_file2.seek(0)
                    json.dump(data, json_file2, indent=4)
        else:
            return_msg = 'Invalid Input'
            
        return return_msg

    def deposit(self, uid, account_num, amount):
        """
            Deposit funds into a valid account for an existing user

        Args:
            uid:
                The user ID of the account which funds are being deposited into
            account_num:
                The account number for which funds are being deposited into
            amount:
                The amount of funds being deposited
        Returns:
            The account type which is either chequings or savings is returned to the controller, which is then saved
            to the transaction log

        """
        account_type = ''
        if self.checkFloat(amount):
            with open('model/account_model.json') as json_file:
                data = json.load(json_file)
            for index, account in enumerate(data):
                if (account['uid'] == uid) and (account['acc_num'] == account_num):
                    account_type = account['acc_type']
                    curr_amount = float(data[index]['acc_balance'])
                    new_amount = round(curr_amount + float(amount), 2)
                    data[index]['acc_balance'] = str(new_amount)
            with open('model/account_model.json', 'w') as json_file2:
            
                json_file2.seek(0)
                json.dump(data, json_file2, indent=4)
        return account_type

    def getBalance(self, uid, account_num):
        """
            Request the account balance when given a valid user ID and account number belonging to that user

        Args:
            uid:
                The user ID which owns an account we want to see the balance of
            account_num:
                The account number for which the current balance is being requested

        Returns:
            A float which is the current balance of the requested account
        """
        with open('model/account_model.json', 'r+') as json_file:
            data = json.load(json_file)
            for index, account in enumerate(data):
                if (account['uid'] == uid) and (account['acc_num'] == account_num):
                    return round(float(data[index]['acc_balance']), 2)

    def checkFloat(self, value):
        """
            This function checks if the value can be made into a float, then checks to see if the value is greater
            than or equal to zero.
        Args:
            value:
                Can be an int, float, or string
        Returns:
            Returns True if the value is greater than or equal to zero, and can be made into a float, and False
            otherwise
        """
        try:
            if float(value) >= 0.0:
                return True
            else:
                print('Invalid value, please re-enter amount.')
                return False
        except ValueError:
            print('Invalid value, please re-enter amount.')
            return False

    def getAccountType(self, uid, acc_num):
        self.loadAccount()
        for acc in self.accounts:
            if acc['uid'] == uid and acc['acc_num'] == acc_num:
                return acc['acc_type']

        return ''

if __name__ == '__main__':
    am = AccountModel()
    am.createNewAccount('Chequing','Chequing')
