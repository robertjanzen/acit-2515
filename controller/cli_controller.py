from model.chequing_model import Chequing
from model.saving_model import Saving
from model.term_model import TermSaving
from view.cli_view import CLIView
from model.cli_db import CLIDB


class CLIController():

    def __init__(self):
        self.view = CLIView()
        self.clidb = CLIDB()

    def run(self):
        user_name = self.view.getCLIName()
        if self.clidb.verifyCLIName(user_name):
            password = self.view.getCLIPwd()
            if self.clidb.verifyPwd(password):
                print('Successfully logged in.')
                self.menu()


    def menu(self):
        menu_input = self.view.showMenu()
        if menu_input == 1:
            self.cli_manage()
        elif menu_input == 2:
            self.cli_create()
        elif menu_input == 3:
            exit(0)

    def cli_manage(self):
        pass

    def cli_create(self):
        pass





if __name__ == "__main__":
    controller = CLIController()
    controller.run()
    # while True:
    #     controller.run()