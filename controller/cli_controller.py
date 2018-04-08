from model.chequing_model import Chequing
from model.saving_model import Saving
from model.account_model import AccountModel
from view.cli_view import CLIView
from model.cli_db import CLIDB


class CLIController:

    def __init__(self):
        self.view = CLIView()
        self.clidb = CLIDB('model/cli_acc_db.csv')
        self.accounts = AccountModel()

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
            balance = AccountModel.get_balance(uid, accNum)
            self.view.showBalance(balance)


    def cli_create_acc(self, uid):
        tInput = self.view.getAccType()
        if tInput == '1':
            accType = 'Chequing'
        elif tInput == '2':
            accType = 'Saving'
        elif tInput == '3':
            exit(0)
        accName = self.view.getAccName()
        initDep = self.view.getDeposit()
        self.accounts.create_new_account(accType, accName, initDep, uid)

    def cli_new_uid(self):
        pass

    #
    # def cli_trans_report(self):
    #     pass
    #
    # def cli_manage(self):
    #     mInput = self.view.getManInput()
    #     if mInput == '1':
    #         self.cli_create_user()
    #     elif mInput == '2':
    #         self.cli_manage_user()
    #     elif mInput == '4':
    #         exit(0)
    #
    # def cli_create_user(self):
    #     pass
    #
    # def cli_deposit(self):
    #     uid = self.view.uidInput()
    #     accNum = self.view.accNumInput()
    #     amount = self.view.depositInput()
    #     self.accounts.deposit(uid, accNum, amount)
    #
    # def cli_create(self):
    #     account_input = self.view.accountType()
    #     if account_input == '1':
    #         pass
    #     elif account_input == '2':
    #         self.create_saving()
    #     elif account_input == '3':
    #         pass
    #     elif account_input == '4':
    #         exit(0)
    #
    # def create_chequing(self):
    #     accName = self.view.getAccName()
    #     deposit = self.view.getInitialDeposit()
    #     # new_account = AccountModel()
    #     # new_account.create_new_account('10', '1010', 'Chequing', accName, deposit)
    #     print(accName, deposit)
    #
    # def create_saving(self):
    #     print('This creates a saving account')


if __name__ == "__main__":
    controller = CLIController()
    controller.run()
    # while True:
    #     controller.run()