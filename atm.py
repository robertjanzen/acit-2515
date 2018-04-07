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
    trans_model = TransactionModel()
    account_model = AccountModel()
    usr_db = UserDB(USER_DB_FILE)
    
    test_acc_db = [
    {
            'uid': '1',
            'acc_num': '1001',
            'acc_type': 'Chequing',
            'acc_name': 'Chequing',
            'acc_balance': 10
        },
        {
            'uid': '1',
            'acc_num': '1002',
            'acc_type': 'Savings',
            'acc_name': 'Savings',
            'acc_balance': 100
        },
        {
            'uid': '2',
            'acc_num': '1003',
            'acc_type': 'Chequing',
            'acc_name': 'Chequing',
            'acc_balance': 10
        },
        {
            'uid': '2',
            'acc_num': '1004',
            'acc_type': 'Savings',
            'acc_name': 'Savings1',
            'acc_balance': 100
        },
        {
            'uid': '2',
            'acc_num': '1005',
            'acc_type': 'Savings2',
            'acc_name': 'Savings2',
            'acc_balance': 100
        },
        {
            'uid': '2',
            'acc_num': '1006',
            'acc_type': 'Savings3',
            'acc_name': 'Savings3',
            'acc_balance': 100
        },
        {
            'uid': '2',
            'acc_num': '1007',
            'acc_type': 'Savings4',
            'acc_name': 'Savings4',
            'acc_balance': 100
        },
        {
            'uid': '2',
            'acc_num': '1008',
            'acc_type': 'VIP Chequing',
            'acc_name': 'VIP',
            'acc_balance': 1000000000
        }
    ]
    
    atm_btn_controller = ButtonController(atm_View, state_db)
    atm_login_ctrl = LoginController(atm_View, state_db, usr_db)
    atm_trans_ctrl = TransactionController(atm_View, state_db, account_model, trans_model)
    
    state_db.state = "Card"
    mainloop()
