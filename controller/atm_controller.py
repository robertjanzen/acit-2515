from view.atm_view import View as atm_view
from tkinter import *
from observe.observer import Observer

class LoginController:
    _ControllerState = 1
    _Target_UID = -1
    
    def __init__(self, master, db):
        self.view = atm_view(master)
        self.db = db
        self.update()
        self.keypad_binding()
        self.view.lb3.configure(command= self.cancel_session)

    def keypad_binding(self):
        self.view.npb1.configure(command=lambda: self.keypad_entry(1))
        self.view.npb2.configure(command=lambda: self.keypad_entry(2))
        self.view.npb3.configure(command=lambda: self.keypad_entry(3))
        self.view.npb4.configure(command=lambda: self.keypad_entry(4))
        self.view.npb5.configure(command=lambda: self.keypad_entry(5))
        self.view.npb6.configure(command=lambda: self.keypad_entry(6))
        self.view.npb7.configure(command=lambda: self.keypad_entry(7))
        self.view.npb8.configure(command=lambda: self.keypad_entry(8))
        self.view.npb9.configure(command=lambda: self.keypad_entry(9))
        self.view.npb10.configure(command=self.delete_entry)
        self.view.npb11.configure(command=lambda: self.keypad_entry(0))
        self.view.npb12.configure(command=self.confirm)
    
    def keypad_entry(self, input_value):
        if self._ControllerState != 3:
            self.view.mid_title_input.insert(END, input_value)

    def confirm(self):
        entry = self.view.mid_title_input.get()
        
        if self._ControllerState == 1:
            self.check_card_num(entry)
        elif self._ControllerState == 2:
            self.check_pin(entry)
        else:
            pass
    
    def cancel_session(self):
        if self._ControllerState != 1:
            self._ControllerState = 1
            self.update()
    
    def check_card_num(self, input_number):
        for account in self.db:
            if account["card_number"] == input_number:
                self._Target_UID = account["uid"]
                
                self._ControllerState = 2
        self.update()
    
    def check_pin(self, input_PIN):
        target_account = {}
        for account in self.db:
            if account["uid"] == self._Target_UID:
                target_account = account
                break
        print(target_account)
        if target_account["PIN"] == input_PIN:
            self._ControllerState = 3
            
        self.update()
    
    def delete_entry(self):
        if self._ControllerState != 3:
            last_index = len(self.view.mid_title_input.get()) - 1
            self.view.mid_title_input.delete(last_index)

    def update(self):
        current_state = self._ControllerState
        
        if current_state == 1:
            self._Target_UID = -1
            self.view.render_card_entry()
            
        elif current_state == 2:
            self.view.render_PIN_entry()
            
        elif current_state == 3:
            self.view.render_acc_info_page("sample account", "sample type", "1111111111")


if __name__ == '__main__':
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

    test_controller = LoginController(root, test_db)
    
    mainloop()
