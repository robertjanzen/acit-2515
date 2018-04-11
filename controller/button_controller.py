# button_controller.py
#
# ATM MVC program
#
# Team alroda
#
# Aldrich Huang A01026502 2B
# Robert Janzen A01029341 2B
# David Xiao A00725026 2B

from observe.observer import Observer

class ButtonController(Observer):

    def __init__(self, view, state_model):
        self.view = view
        self.state_db = state_model
        self.keypad_binding()
        self.state_db.add_observer(self)

    def keypad_binding(self):
        """
            Configures the commands for the buttons and keypads
            
        Returns:
            None
        """
        
        self.view.rb1.configure(command=lambda: self.button_input(self.view.ml4.cget("text")))
        self.view.rb2.configure(command=lambda: self.button_input(self.view.ml8.cget("text")))
        self.view.rb3.configure(command=lambda: self.button_input(self.view.ml12.cget("text")))

        self.view.lb1.configure(command=lambda: self.button_input(self.view.ml1.cget("text")))
        self.view.lb2.configure(command=lambda: self.button_input(self.view.ml5.cget("text")))
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
        self.view.npb10.configure(command=lambda: self.input_cmd("DEL"))
        self.view.npb11.configure(command=lambda: self.keypad_entry(0))
        self.view.npb12.configure(command=lambda: self.input_cmd("OK"))

    def button_input(self, btn_input):
        """
            Sends button input to state model. Originally planned to be more logic here
            
        Args:
            btn_input:
                Input value representing the command to be executed when button is clicked
                
        Returns:
            None
        """
        
        self.input_cmd(btn_input)

    def keypad_entry(self, input_value):
        """
            Sends keypad entry to state model
            
        Args:
            input_value:
                Input value representing the value entered by the keypad
                
        Returns:
            None
        """
        
        
        self.state_db.entry = input_value

    def input_cmd(self, user_input):
        """
            Sends input to the state model
            
        Args:
            user_input:
                Input value representing the command to be executed when button is clicked
                
        Returns:
            None
        """
        
        self.state_db.input = user_input

    def cancel_session(self):
        """
            Sets the state of the atm to the Card state
            
        Returns:
            None
        """
        
        if self.state_db != "Card":
            self.state_db.state = "Card"

    def update(self, publisher, **kwargs):
        # Used for testing purposes
        pass
