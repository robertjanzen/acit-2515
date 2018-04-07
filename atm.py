from tkinter import *
from view.atm_view import View as atm_view

from model.state_model import StateModel
from model.user_model import UserDB
from model.transaction_model import TransactionModel
from model.account_model import AccountModel

from controller.button_controller import ButtonController
from controller.login_controller import LoginController
from controller.transaction_controller import TransactionController

from constants import *

if __name__ == "__main__":
    root = Tk()
    atm_View = atm_view(root)

    state_db = StateModel()
    account_model = AccountModel()
    trans_model = TransactionModel()
    usr_db = UserDB(USER_DB_FILE)

    atm_btn_controller = ButtonController(atm_View, state_db)
    atm_login_ctrl = LoginController(atm_View, state_db, usr_db)
    atm_trans_ctrl = TransactionController(atm_View, state_db, account_model, trans_model)
    
    state_db.state = "Card"
    mainloop()
