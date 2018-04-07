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
        self.add_user_to_db(user_object)

    def add_user_to_db(self, user_object):
        with open('user_db.json') as json_file:
            data = json.load(json_file)
            data.append(user_object)

        with open('user_db.json', 'w') as out_file:
            json.dump(data, out_file)

    def delete_account(self):
        pass

    def update_acc_balance(self, uid, acc_num, acc_type, amount):
        pass

if __name__ == '__main__':
    am = AccountModel()
    am.create_new_account('1','1001','Chequing','Chequing')