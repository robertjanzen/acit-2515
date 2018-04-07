from tkinter import *
from view.atm_view import View as atm_view
from model.state_model import StateModel
from controller.button_controller import ButtonController
from controller.login_controller import LoginController

if __name__ == "__main__":
    root = Tk()
    test_db = [
        {
            "uid": 1,
            "card_number": "1001",
            "PIN": "123456789"
        },
        {
            "uid": 2,
            "card_number": "1002",
            "PIN": "987654321"
        }
    ]
    atm_View = atm_view(root)
    state_db = StateModel()
    atm_btn_controller = ButtonController(atm_View, state_db)
    atm_login_ctrl = LoginController(atm_View, state_db, test_db)
    state_db.state = 1
    mainloop()