# state_model.py
#
# ATM MVC program
#
# Team alroda
#
# Aldrich Huang A01026502 2B
# Robert Janzen A01029341 2B
# David Xiao A00725026 2B


from observe.observer import Observable


class StateModel(Observable):
    def __init__(self):
        super().__init__()
        self._state = ''
        self._entry = -1
        self._input = -1
        self._session_uid = -1
        self._prev_states = []
        self._usr_acc_dict = {}
        
    def reset(self):
        """
            Resets the instance variables used for ATM operation
            
        Returns:
            None
        """
        
        self._entry = -1
        self._input = -1
        self.uid = -1
        self._usr_acc_dict = {}
        
    @property
    def prev_state(self):
        """
            Getter used to get the previous state that the ATM is in
            
        Returns:
            String represented the previous state that the ATM is in
        """
        
        record_size = len(self._prev_states)
        if record_size > 1:
            output = self._prev_states[record_size - 2]
        else:
            output = 'Card'
        return output
    
    @prev_state.setter
    def prev_state(self, input_value):
        """
            Setter for setting the previous state list for the ATM
            
        Args:
            input_value:
                State to be added to the previous state list
                
        Returns:
            None
        """
        
        if input_value in self._prev_states:
            index = self._prev_states.index(input_value)
            self._prev_states = self._prev_states[0:index + 1]
        else:
            self._prev_states.append(input_value)
            

    @property
    def state(self):
        """
            Getter for the instance variable: self._state
        Returns:
            Value of self._state
        """
        
        return self._state

    @state.setter
    def state(self, input_value):
        """
            Setter for setting the value of the instance variable self._state
            
        Args:
            input_value:
                New value for self._state
                
        Returns:
            None
        """
        
        self._state = input_value
        self.prev_state = self.state
        self.notify_all(state=input_value)

    @property
    def entry(self):
        """
            Getter for the instance variable: self._entry
            
        Returns:
            Value of self._entry
        """
        
        return self._entry

    @entry.setter
    def entry(self, input_value):
        """
            Setter for setting the value of the instance variable self._entry
            
        Args:
            input_value:
                New value for self._entry
            
        Returns:
            None
        """
        
        self._entry = input_value
        self.notify_all(entry=input_value)

    @property
    def input(self):
        """
            Getter for the instance variable: self._input
        Returns:
            Value of self._input
        """
        
        return self._input

    @input.setter
    def input(self, input_value):
        """
            Setter for setting the value of the instance variable self._input
        Args:
            input_value:
                New value for self._input
        Returns:
            None
        """
        
        self._input = input_value
        self.notify_all(input=input_value)

    @property
    def uid(self):
        """
            Getter for the instance variable: self._uid
            
        Returns:
            Value of self._uid
        """
        
        return self._session_uid

    @uid.setter
    def uid(self, input_value):
        """
            Setter for the instnace variable self._uid
            
        Args:
            input_value:
                New value for self._uid

        Returns:
            None
        """
        
        self._session_uid = input_value
        
    @property
    def usr_record(self):
        """
            Getter for the instance variable self._usr_acc_dict
            
        Returns:
            None
        """
        return self._usr_acc_dict
    
    @usr_record.setter
    def usr_record(self, input_value):
        """
            Setter for the instance variable self._usr_acc_dict
            
        Args:
            input_value:
                New value for self._usr_acc_dict
                
        Returns:
            None
        """
        
        self._usr_acc_dict = input_value
    
    def __str__(self):
        """
            Returns state information
            
        Returns:
            String containing state information
        """
        
        return "State: {}\nEntry: {}\nInput: {}".format(self.state, self.entry, self.input);
