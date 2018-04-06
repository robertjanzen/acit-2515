class StateModel:
    def __init__(self):
        self._state = 1;
        self._entry = -1;
        self._input = -1;

    @property
    def state(self):
        return self._state

    @property.setter
    def state(self, input_value):
        self._state = input_value

    @property
    def entry(self):
        return self._entry

    @property.setter
    def entry(self, input_value):
        self._entry = input_value

    @property
    def input(self):
        return self._input

    @property.setter
    def input(self, input_value):
        self._input = input_value
