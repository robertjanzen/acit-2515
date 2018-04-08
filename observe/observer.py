# observer.py
#
# ATM MVC program
#
# Team alroda
#
# Aldrich Huamg A01026502 2B
# Robert Janzen A01029341 2B
# David Xiao A00725026 2B


class Observer:
    def update(self, obj, **kwargs):
        raise NotImplementedError


class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Error: Failed to add: {}'.format(observer))

    def remove_observer(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Error: Failed to remove: {}'.format(observer))

    def notify_all(self, **kwargs):
        for observer in self.observers:
            observer.update(self, **kwargs)
