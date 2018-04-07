from tkinter import *
from observe.observer import Observer


class LoginController(Observer):
    def __init__(self, view, state_model, user_db):
        self.view = view
        self.state_db = state_model
        self.state_db.add_observer(self)

        self.db = user_db.db_content

    def check_card_num(self, input_number):
        for account in self.db:
            if account["card_number"] == input_number:
                self.state_db.uid = account["uid"]
                self.state_db.state = "PIN"
            else:
                self.state_db.state = 'Card'

    def check_pin(self, input_PIN):
        target_account = {}
        for account in self.db:
            if account["uid"] == self.state_db.uid:
                target_account = account
                break
        if self.unhash(target_account["PIN"]) == input_PIN:
            self.state_db.state = "Overview"
        else:
            self.state_db.state = "PIN"
            
    @staticmethod
    def unhash(input_hash):
        num_str = ''
        curr_num = ''
        for character in input_hash:
            if int(character) % 2 != 0 and int(character) != 1:
                if curr_num != '':
                    num_str += str(int(int(curr_num)/2))
                    curr_num = ''
            else:
                curr_num += character
        num_str += str(int(int(curr_num)/2))
        return num_str

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
                self.view.render_card()

            elif new_state == "PIN":
                self.view.render_pin()
