from view.atm_view import View as atm_view
from model.state_model import StateModel
from tkinter import *


class ADC:

    def __init__(self, master):
        self.view = atm_view(master)
        self.state_db = StateModel()
        self.keypad_binding()

    def keypad_binding(self):
        self.view.rb1.configure(command=self.button_input(self.view.ml4.cget("text")))
        self.view.rb2.configure(command=self.button_input(self.view.ml8.cget("text")))
        self.view.rb3.configure(command=self.button_input(self.view.ml12.cget("text")))

        self.view.lb1.configure(command=self.button_input(self.view.ml1.cget("text")))
        self.view.lb2.configure(command=self.button_input(self.view.ml5.cget("text")))
        self.view.lb3.configure(command=self.cancel_session)

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

    def button_input(self, btn_input):
        self.state_db.input = btn_input

    def keypad_entry(self, input_value):
        self.state_db.entry = input_value

    def cancel_session(self):
        self.state_db.state = 1

    def confirm(self):
        self.state_db.input = "OK"


if __name__ == "__main__":
    root = Tk()

    test_controller = ADC(root)

    mainloop()