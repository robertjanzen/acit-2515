from observe.observer import Observable


class StateModel(Observable):
    def __init__(self):
        super().__init__()
        self._state = '';
        self._entry = -1;
        self._input = -1;
        self._session_uid = -1

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, input_value):
        self._state = input_value
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

    def __str__(self):
        return "State: {}\nEntry: {}\nInput: {}".format(self.state, self.entry, self.input);
