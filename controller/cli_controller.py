from model.account_model import AccountModel
from view.cli_view import CLIView
from model.cli_db import CLIDB
from model.user_model import UserDB
import random


class CLIController:

    def __init__(self):
        self.view = CLIView()
        self.clidb = CLIDB('model/cli_acc_db.csv')
        self.accounts = AccountModel()
        self.userdb = UserDB('model/user_db.csv')

    def run(self):
        user_name = self.view.getCLIName()
        password = self.view.getCLIPwd()
        if self.clidb.verify_account(user_name, password):
            print('Successfully logged in.')
            self.uidMenu()
        else:
            print('Incorrect username password combination')

    def uidMenu(self):
        """Manage user or create new user"""
        uInput = self.view.showUidMenu()
        if uInput == '1':
            self.cli_uid_menu()
        elif uInput == '2':
            self.cli_new_uid()
        elif uInput == '3':
            exit(0)

    def cli_uid_menu(self):
        uid = self.view.getUid()
        self.cli_acc_menu(uid)

    def cli_acc_menu(self, uid):
        aInput = self.view.showAccMenu()
        if aInput == '1':
            self.cli_man_acc(uid)
        elif aInput == '2':
            self.cli_create_acc(uid)
        elif aInput == '3':
            exit(0)

    def cli_man_acc(self, uid):
        accNum = self.view.getAccNum()
        maInput = self.view.showManAccMenu()
        if maInput == '1':
            amount = self.view.getDeposit()
            self.accounts.deposit(uid, accNum, amount)
        elif maInput == '2':
            amount = self.view.getWithdraw()
            self.accounts.withdraw(uid, accNum, amount)
        elif maInput == '3':
            balance = self.accounts.get_balance(uid, accNum)
            self.view.showBalance(balance)


    def cli_create_acc(self, uid):
        tInput = self.view.getAccType()
        if tInput == '1':
            accType = 'Chequing'
        elif tInput == '2':
            accType = 'Savings'
        elif tInput == '3':
            exit(0)
        accName = self.view.getAccName()
        initDep = self.view.getDeposit()
        self.accounts.create_new_account(accType, accName, initDep, uid)

    def cli_new_uid(self):
        tInput = self.view.getAccType()
        if tInput == '1':
            accType = 'Chequing'
        elif tInput == '2':
            accType = 'Savings'
        elif tInput == '3':
            exit(0)
        accName = self.view.getAccName()
        initDep = self.view.getDeposit()
        uid = self.accounts.create_new_account(accType, accName, initDep)
        self.create_user_db(uid)

    def create_user_db(self, uid):
        cardNum = self.generate_cardNum(uid)
        pwdHash = self.hash_password()
        self.userdb.create_new_entry(uid, cardNum, pwdHash)

    def generate_cardNum(self, uid):
        init_cardNum = 10000000
        cardNum = init_cardNum+int(uid)
        return str(cardNum)

    def get_password(self):
        inputPwd = self.view.getPIN()
        inputPwd2 = self.view.confirmPIN()
        if inputPwd == inputPwd2:
            return inputPwd

    def hash_password(self):
        pwd = self.get_password()
        hash_str = str(int(pwd[0])*2)
        odd_num = ['3', '5', '7', '9']
        for strIndex in range(1,len(pwd)):
            odd_str = ''
            for rand_num in range(random.randint(1,6)):
                odd_str += random.choice(odd_num)
            hash_str +=(odd_str+str(int(pwd[strIndex])*2))
        return hash_str

if __name__ == "__main__":
    controller = CLIController()
    controller.run()
    # while True:
    #     controller.run()