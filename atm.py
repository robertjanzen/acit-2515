from tkinter import *
from view.atm_view import View as atm_view
from model.state_model import StateModel
from controller.adc import ADC

if __name__ == "__main__":
    root = Tk()

    state_db = StateModel()
    atm_ADC = ADC(root, state_db)
    mainloop()