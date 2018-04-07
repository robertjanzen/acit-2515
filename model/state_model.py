from observe.observer import Observable


class StateModel(Observable):
    def __init__(self):
        super().__init__()
        self._state = ''
        self._entry = -1
        self._input = -1
        self._session_uid = -1
        self._prev_states = []
        
    def reset(self):
        self._entry = -1
        self._input = -1
        self.uid = -1
        
    @property
    def prev_state(self):
        record_size = len(self._prev_states)
        if record_size > 1:
            output = self._prev_states[record_size - 2]
        else:
            output = 'Card'
        return output
    
    @prev_state.setter
    def prev_state(self, input_value):
        print(input_value)
        if input_value in self._prev_states:
            index = self._prev_states.index(input_value)
            self._prev_states = self._prev_states[0:index + 1]
        else:
            self._prev_states.append(input_value)
            

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, input_value):
        self._state = input_value
        self.prev_state = self.state
        self.notify_all(state=input_value)

    @property
    def entry(self):
        return self._entry

    @entry.setter
    def entry(self, input_value):
        self._entry = input_value
        self.notify_all(entry=input_value)

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, input_value):
        self._input = input_value
        self.notify_all(input=input_value)

    @property
    def uid(self):
        return self._session_uid

    @uid.setter
    def uid(self, input_value):
        self._session_uid = input_value
        
    @property
    def usr_record(self):
        return self._usr_acc_dict
    
    @usr_record.setter
    def usr_record(self, input_value):
        self._usr_acc_dict = input_value
    
    def __str__(self):
        return "State: {}\nEntry: {}\nInput: {}".format(self.state, self.entry, self.input);
