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
        input = self.view.showUidMenu()
        if input == '1':
            self.cli_uid_menu()
        elif input == '2':
            self.cli_new_uid()
        elif input == '3':
            exit(0)

    def cli_uid_menu(self):
        input = self.view.showManUid()
        if input == '1':
            self.cli_man_uid()
        elif input == '2':
            self.cli_new_uid()
        elif input == '3':
            self.cli_trans_report()
        elif input == '4':
            exit(0)

    def cli_man_uid(self):
        uInput = self.view.getManInput()
        if uInput == '1':
            self.cli_create_user()
        elif uInput == '2':
            self.cli_manage_user()
        elif uInput == '3':
            exit(0)

    def cli_new_uid(self):
        uInput = self.view.getManInput()
        if uInput == '1':
            self.cli_create_user()
        elif uInput == '2':
            self.cli_manage_user()
        elif uInput == '3':
            exit(0)

    def cli_manage(self):
        mInput = self.view.getManInput()
        if mInput == '1':
            self.cli_create_user()
        elif mInput == '2':
            self.cli_manage_user()
        elif mInput == '4':
            exit(0)
            
    def cli_create_user(self):
        pass

    def cli_deposit(self):
        uid = self.view.uidInput()
        accNum = self.view.accNumInput()
        amount = self.view.depositInput()
        self.accounts.deposit(uid, accNum, amount)

    def cli_create(self):
        account_input = self.view.accountType()
        if account_input == '1':
            pass
        elif account_input == '2':
            self.create_saving()
        elif account_input == '3':
            pass
        elif account_input == '4':
            exit(0)

    def create_chequing(self):
        accName = self.view.getAccName()
        deposit = self.view.getInitialDeposit()
        # new_account = AccountModel()
        # new_account.create_new_account('10', '1010', 'Chequing', accName, deposit)
        print(accName, deposit)

    def create_saving(self):
        print('This creates a saving account')


if __name__ == "__main__":
    controller = CLIController()
    controller.run()
    # while True:
    #     controller.run()