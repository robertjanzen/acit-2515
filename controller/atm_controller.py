from view.atm_view import View as atm_view
from tkinter import *

class LoginController:
    _PAGE_NUMBER = 1
    def __init__(self):
        self.root = Tk()
        self.view = atm_view(self.root)
        self.view.npb12.configure(command=self.cycle)

    def cycle(self):
    
           curr_page = self._PAGE_NUMBER
           if curr_page == 1:
               self.view.master.title('Enter Card Page')
               self.view.render_page1()
           elif curr_page == 2:
               self.view.master.title('Enter PIN Page')
               self.view.render_page2()
           elif curr_page == 3:
               self.view.master.title('Select Account Page')
               self.view.render_page3()
           elif curr_page == 4:
               self.view.master.title('Account Overview and Select Transaction Page')
               self.view.render_page4()
           elif curr_page == 5:
               self.view.master.title('Info Page')
               self.view.render_info_page()
           elif curr_page == 6:
               self.view.master.title('Enter Deposit Amount Page')
               self.view.render_page5()
           elif curr_page == 7:
               self.view.master.title('Select Withdraw Amount Page')
               self.view.render_page6()
           elif curr_page == 8:
               self.view.master.title('Done Page')
               self.view.render_page7()
    
           self._PAGE_NUMBER += 1
           if self._PAGE_NUMBER >= 9:
               self._PAGE_NUMBER = 1

if __name__ == '__main__':
    test = LoginController()
    test.cycle()
    mainloop()
    print('Controller')
    