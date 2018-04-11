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
        self.state_model = state_model
        self.state_model.addObserver(self)
        self._usr_db = user_db
        self._db = self._usr_db.model_content
        
        self.msg = ''

    def checkCardNum(self, input_number):
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
                self.state_model.uid = account["uid"]
                self.state_model.state = "PIN"
                return
            
        self.msg = 'Invalid Card Number'
        self.state_model.state = 'LoginError'

    def checkPin(self, input_PIN):
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
            if account["uid"] == self.state_model.uid:
                target_account = account
                break

        if self.reverseHash(target_account["PIN"]) == partial_hash:
            self.state_model.state = "Selection"

        else:
            self.msg = 'Invalid PIN'
            self.state_model.state = "LoginError"
            
    @staticmethod
    def reverseHash(input_hash):
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
        self._usr_db.openModelFile()
        self._db = self._usr_db.model_content
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

            if self.state_model.state == "Card" or self.state_model.state == "PIN":
                self.view.mid_title_input.insert(END, input_value)

        elif 'input' in updated_data:
            inputCmd = kwargs['input']
            if self.state_model.state == "Card" or self.state_model.state == "PIN":
                if inputCmd == 'DEL':
                    last_index = len(self.view.mid_title_input.get()) - 1
                    self.view.mid_title_input.delete(last_index)

                elif inputCmd == 'OK':
                    entry = self.view.mid_title_input.get()

                    if self.state_model.state == "Card":
                        self.checkCardNum(entry)
                    elif self.state_model.state == "PIN":
                        self.checkPin(entry)
                    else:
                        pass

        elif 'state' in updated_data:
            new_state = kwargs['state']
            if new_state == "Card":
                self.state_model.reset()
                self.view.renderCard()

            elif new_state == "PIN":
                self.view.renderPin()
            
            elif new_state == "LoginError":
                self.view.renderError(self.msg)
