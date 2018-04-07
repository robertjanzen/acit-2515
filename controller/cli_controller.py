from model.chequing_model import Chequing
from model.saving_model import Saving
from model.term_model import TermSaving
from model.account_model import AccountModel
from view.cli_view import CLIView
from model.cli_db import CLIDB


class CLIController():

    def __init__(self):
        self.view = CLIView()
        self.clidb = CLIDB()
        self.accounts = AccountModel()

    def run(self):
        user_name = self.view.getCLIName()
        if self.clidb.verifyCLIName(user_name):
            password = self.view.getCLIPwd()
            if self.clidb.verifyPwd(password):
                print('Successfully logged in.')
                self.menu()

    def menu(self):
        menu_input = self.view.showMenu()
        if menu_input == '1':
            self.cli_manage()
        elif menu_input == '2':
            self.cli_create()
        elif menu_input == '3':
            exit(0)

    def cli_manage(self):
        manInput = self.view.getManInput()
        if manInput == '1':
            self.cli_deposit()
        elif manInput == '2':
            exit(0)

    def cli_deposit(self):
        uid = self.view.uidInput()
        accNum = self.view.accNumInput()
        amount = self.view.depositInput()
        self.accounts.deposit(uid, accNum, amount)

    def cli_create(self):
        account_input = self.view.accountType()
        if account_input == '1':
            self.create_chequing()
        elif account_input == '2':
            self.create_saving()
        elif account_input == '3':
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