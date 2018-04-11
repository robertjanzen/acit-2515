# login_controller.py
#
# ATM MVC program
#
# Team alroda
#
# Aldrich Huang A01026502 2B
# Robert Janzen A01029341 2B
# David Xiao A00725026 2B

from tkinter import *
from observe.observer import Observer

class LoginController(Observer):
    def __init__(self, view, state_model, user_db):
        self.view = view
        self.state_db = state_model
        self.state_db.add_observer(self)
        self._usr_db = user_db
        self._db = self._usr_db.db_content
        
        self.msg = ''

    def check_card_num(self, input_number):
        """
            Checks the inputted card number to see if it is a valid card number
            
        Args:
            input_number:
                Card Number entered at the Card Entry page
                
        Returns:
            None
        """
        
        for account in self.db:
            if account["card_number"] == input_number:
                self.state_db.uid = account["uid"]
                self.state_db.state = "PIN"
                return
            
        self.msg = 'Invalid Card Number'
        self.state_db.state = 'LoginError'

    def check_pin(self, input_PIN):
        """
            Checks the PIN to see if it matches
            
        Args:
            input_PIN:
                PIN entered at the PIN Entry page
                
        Returns:
            None
        """
        target_account = {}

        partial_hash = ''

        for digit in input_PIN:
            partial_hash += str(int(digit) * 2)

        for account in self.db:
            if account["uid"] == self.state_db.uid:
                target_account = account
                break

        if self.unrand(target_account["PIN"]) == partial_hash:
            self.state_db.state = "Selection"

        else:
            self.msg = 'Invalid PIN'
            self.state_db.state = "LoginError"
            
    @staticmethod
    def unrand(input_hash):
        """
            Function for removing randomized dummy values from the hashed PIN
            
        Args:
            input_hash:
                Hashed PIN
                
        Returns:
            Clean Hashed PIN
        """
        
        num_str = ''
        curr_num = ''
        for character in input_hash:
            if int(character) % 2 != 0 and int(character) != 1:
                if curr_num != '':
                    num_str += str(curr_num)
                    curr_num = ''
            else:
                curr_num += character

        if curr_num != '':
            num_str += str(curr_num)

        return num_str

    @property
    def db(self):
        self._usr_db.open_db_file()
        self._db = self._usr_db.db_content
        return self._db

    def update(self, publisher, **kwargs):
        """
            Updates the ATM view
            
        Args:
            publisher:
                Object that is updated
            **kwargs:
                The updated attribute name and value as reported by the observer
                
        Returns:
            None
        """
        
        updated_data = kwargs.keys()

        if 'entry' in updated_data:
            input_value = kwargs['entry']

            if self.state_db.state == "Card" or self.state_db.state == "PIN":
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
                self.state_db.reset()
                self.view.render_card()

            elif new_state == "PIN":
                self.view.render_pin()
            
            elif new_state == "LoginError":
                self.view.render_error(self.msg)
