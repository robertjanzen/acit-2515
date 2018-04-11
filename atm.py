# atm.py
#
# ATM MVC program
#
# Team alroda
#
# Aldrich Huang A01026502 2B
# Robert Janzen A01029341 2B
# David Xiao A00725026 2B

from tkinter import *
from view.atm_view import View as atm_view
import os

from model.state_model import StateModel
from model.user_model import UserModel
from model.transaction_model import TransactionModel
from model.account_model import AccountModel
from model.cli_model import CLIDB

from controller.button_controller import ButtonController
from controller.login_controller import LoginController
from controller.transaction_controller import TransactionController
# from controller.cli_controller import CLIController

from constants import *

if __name__ == "__main__":
    root = Tk()
    atm_View = atm_view(root)

    state_model = StateModel()
    account_model = AccountModel()
    trans_model = TransactionModel()
    usr_db = UserModel(USER_DB_FILE)

    atm_btn_controller = ButtonController(atm_View, state_model)
    atm_login_ctrl = LoginController(atm_View, state_model, usr_db)
    atm_trans_ctrl = TransactionController(atm_View, state_model, account_model, trans_model)
    
    state_model.state = "Card"

    cwd = os.getcwd()
    print(cwd)
    mainloop()
