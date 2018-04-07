import json

class AccountModel:

    def __init__(self):
        pass

    def create_new_account(self):
        with open('user_db.json') as json_file:
            data = json.load(json_file)
            print(json.dumps(data, indent=4))

    def delete_account(self):
        pass

    def update_acc_balance(self, uid, acc_num, acc_type, amount):
        pass

if __name__ == '__main__':
    am = AccountModel()
    am.create_new_account()