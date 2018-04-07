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

if __name__ == '__main__':
    am = AccountModel()
    am.create_new_account('1','1002','Chequing','Chequing')