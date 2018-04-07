import json

class AccountModel:

    def __init__(self):
        pass

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
        with open('account_db.json') as json_file:
            data = json.load(json_file)
            data.append(user_object)

        with open('account_db.json', 'w') as out_file:
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

    def deposit(self, amount):
        """allow deposit if valid amount"""
        # if self.check_float(amount):
        #     self._balance += amount
        #     # self.add_entry('deposit', amount)

    def get_balance(self):
        """print out the current balance"""
        pass

    def check_float(self, value):
        """this function first checks if the value can be made into a float
        then check to see if the value is greater than or equal to 0
        returns false if both criteria are not met so account information is not changed"""
        try:
            float(value)
            if value >= 0:
                return True
            else:
                print('Invalid value, please re-enter amount.')
                return False
        except ValueError:
            print('Invalid value, please re-enter amount.')
            return False

if __name__ == '__main__':
    am = AccountModel()
    am.create_new_account('1','1002','Chequing','Chequing')