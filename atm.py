from tkinter import *
from view.atm_view import View as atm_view
from model.state_model import StateModel
from controller.adc import ADC

if __name__ == "__main__":
    root = Tk()
    atm_View = atm_view(root)
    state_db = StateModel()
    atm_ADC = ADC(atm_View, state_db)
    mainloop()