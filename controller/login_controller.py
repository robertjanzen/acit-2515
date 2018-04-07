from tkinter import *
from observe.observer import Observer


class LoginController(Observer):
    def __init__(self, view, state_model, user_db):
        self.view = view
        self.state_db = state_model
        self.state_db.add_observer(self)

        self.db = user_db

    def check_card_num(self, input_number):
        for account in self.db:
            if account["card_number"] == input_number:
                self.state_db.uid = account["uid"]
                self.state_db.state = "PIN"

    def check_pin(self, input_PIN):
        target_account = {}
        for account in self.db:
            if account["uid"] == self.state_db.uid:
                target_account = account
                break
        print(target_account)
        if target_account["PIN"] == input_PIN:
            self.state_db.state = "Overview"

    def update(self, publisher, **kwargs):
        updated_data = kwargs.keys()

        if 'entry' in updated_data:
            input_value = kwargs['entry']

            if self.state_db.state == "Card" or  self.state_db.state == "PIN":
                self.view.mid_title_input.insert(END, input_value)

        elif 'input' in updated_data:
            input_cmd = kwargs['input']
            if self.state_db.state == "Card" or self.state_db.state == "PIN":
                if input_cmd == 'DEL':
                    last_index = len(self.view.mid_title_input.get()) - 1
                    self.view.mid_title_input.delete(last_index)

                elif input_cmd == 'OK':
                    entry = self.view.mid_title_input.get()

                    if self.state_db.state == "Card":
                        self.check_card_num(entry)
                    elif self.state_db.state == "PIN":
                        self.check_pin(entry)
                    else:
                        pass

        elif 'state' in updated_data:
            new_state = kwargs['state']
            if new_state == "Card":
                self.state_db.uid = -1
                self.view.render_card_entry()

            elif new_state == "PIN":
                self.view.render_PIN_entry()

