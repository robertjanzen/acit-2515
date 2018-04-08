from model.account_model import AccountModel
from view.cli_view import CLIView
from model.cli_db import CLIDB
from model.user_model import UserDB
from model.transaction_model import TransactionModel
import random


class CLIController:

    def __init__(self):
        self.view = CLIView()
        self.clidb = CLIDB('model/cli_acc_db.csv')
        self.accounts = AccountModel()
        self.userdb = UserDB('model/user_db.csv')
        self.trans = TransactionModel()
        self.state = 0
        self.uid = ''
        self.accNum = ''

    def run(self):
        user_name = self.view.getCLIName()
        password = self.view.getCLIPwd()
        if self.clidb.verify_account(user_name, password):
            self.view.success()
            if self.state == 0:
                self.uidMenu()
            elif self.state == 1:
                self.cli_acc_menu()
        else:
            self.view.incorrect()

    def uidMenu(self):
        """Manage user or create new user"""
        uInput = self.view.showUidMenu()
        if uInput == '1':
            self.cli_uid_menu()
        elif uInput == '2':
            self.cli_new_uid()
        elif uInput == '3':
            self.run()
        elif uInput == '4':
            exit(0)

    def cli_uid_menu(self):
        self.uid = self.view.getUid()
        self.cli_acc_menu()

    def cli_acc_menu(self):
        self.state = 1
        aInput = self.view.showAccMenu()
        if aInput == '1':
            self.cli_choose_account()
        elif aInput == '2':
            self.cli_create_acc()
            self.cli_acc_menu()
        elif aInput == '3':
            self.get_report()
            self.cli_acc_menu()
        elif aInput == '4':
            self.uidMenu()
        elif aInput == '5':
            exit(0)

    def cli_choose_account(self):
        self.view.showAccounts(self.uid, self.accounts.accounts)
        self.accNum = self.view.getAccNum()
        self.cli_man_acc()

    def cli_man_acc(self):
        maInput = self.view.showManAccMenu()
        if maInput == '1':
            amount = self.view.getDeposit()
            self.accounts.deposit(self.uid, self.accNum, amount)
            self.view.depositSuccess(amount)
            self.cli_man_acc()
        elif maInput == '2':
            amount = self.view.getWithdraw()
            msg = self.accounts.withdraw(self.uid, self.accNum, amount)
            if msg == '':
                self.view.withdrawSuccess(amount)
            else:
                self.view.withdrawFailure(msg)
            self.cli_man_acc()
        elif maInput == '3':
            balance = self.accounts.get_balance(self.uid, self.accNum)
            self.view.showBalance(balance)
            self.cli_man_acc()
        elif maInput == '4':
            # TODO Charge fee
            self.cli_acc_menu()
        elif maInput == '5':
            self.cli_acc_menu()
        elif maInput == '6':
            exit(0)


    def cli_create_acc(self):
        tInput = self.view.getAccType()
        if tInput == '1':
            accType = 'Chequing'
        elif tInput == '2':
            accType = 'Savings'
        elif tInput == '3':
            self.cli_acc_menu()
        elif tInput == '4':
            exit(0)
        accName = self.view.getAccName()
        initDep = self.view.getDeposit()
        self.accounts.create_new_account(accType, accName, initDep, self.uid)

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
        self.uid = self.accounts.create_new_account(accType, accName, initDep)
        self.create_user_db()
        self.accounts.load_accounts()
        self.uidMenu()

    def create_user_db(self):
        cardNum = self.generate_cardNum(self.uid)
        pwdHash = self.hash_password()
        self.userdb.create_new_entry(self.uid, cardNum, pwdHash)

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

    def get_report(self):
        report = self.trans.display_report(self.uid)
        self.view.printReport(report)

if __name__ == "__main__":
    controller = CLIController()
    controller.run()
    # while True:
    #     controller.run()