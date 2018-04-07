import json

class AccountModel:

    def __init__(self):
        self.accounts = None
        self.load_accounts()

    def load_accounts(self):
        with open('model/account_db.json') as json_file:
            self.accounts = json.load(json_file)

    def create_new_account(self, uid, acc_num, acc_type, acc_name, acc_balance=0):
        user_object = {
            "uid": uid,
            "acc_num": acc_num,
            "acc_type": acc_type,
            "acc_name": acc_name,
            "acc_balance": acc_balance
        }
        self.save_account_to_file(user_object)

    def save_account_to_file(self, user_object):
        exists = False
        with open('model/account_db.json') as json_file:
            data = json.load(json_file)
            for account in data:
                if (account['uid'] == user_object['uid']) and (account['acc_num'] == user_object['acc_num']):
                    exists = True
            if not exists:
                data.append(user_object)
            else:
                print('Account already exists')

        with open('model/account_db.json', 'w') as out_file:
            json.dump(data, out_file)

    def delete_account(self):
        pass

    def update_acc_balance(self, uid, acc_num, acc_type, amount):
        pass

    def change_name(self, accName):
        """changes owner name"""
        pass

    def withdraw(self, amount):
        """allow withdraw if valid amount and sufficient balance, print error message otherwise"""
        # if self.check_float(amount):
        #     if self._balance >= amount:
        #         self._balance -= amount
        #         # self.add_entry('withdraw', amount)
        #     else:
        #         print('Insufficient funds.')

    def deposit(self, uid, account_num, amount):
        """allow deposit if valid amount"""
        if self.check_float(amount):
            with open('model/account_db.json', 'r+') as json_file:
                data = json.load(json_file)
                for index, account in enumerate(data):
                    if (account['uid'] == uid) and (account['acc_num'] == account_num):
                        curr_amount = float(data[index]['acc_balance'])
                        new_amount = curr_amount + float(amount)
                        data[index]['acc_balance'] = str(new_amount)

                json_file.seek(0)
                json.dump(data, json_file)

    def get_balance(self):
        """print out the current balance"""
        pass

    def check_float(self, value):
        """this function first checks if the value can be made into a float
        then check to see if the value is greater than or equal to 0
        returns false if both criteria are not met so account information is not changed"""
        try:
            if float(value) >= 0.0:
                return True
            else:
                print('Invalid value, please re-enter amount.')
                return False
        except ValueError:
            print('Invalid value, please re-enter amount.')
            return False

if __name__ == '__main__':
    am = AccountModel()
    am.create_new_account('1','1004','Chequing','Chequing')
