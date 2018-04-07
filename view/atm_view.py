#
# View.py
#
# Final Project
#

from tkinter import *


class View:
    def __init__(self, master):
        # create any instances of other support classes that are needed and save them
        # as attributes of this window
        self.master = master

        # set main window attributes such as title, geometry etc
        #
        self.master.title('ATM')
        self.master.geometry('515x250')
        self.master.configure(background='grey')

        # set up menus if there are any
        # NO MENUS FOR ATM

        # commands going in the file menu
        # NO MENUS FOR ATM

        # define frames if needed
        self.top_frame = Frame(self.master)
        self.top_left_side_frame = Frame(self.master)
        self.top_middle_frame = Frame(self.master)
        self.top_right_side_frame = Frame(self.master)

        self.bottom_frame = Frame(self.master)

        self.top_frame.grid(row=0, column=0, rowspan=3, columnspan=8, padx=30, pady=30)
        self.top_left_side_frame.grid(row=0, column=0, rowspan=3, columnspan=2, padx=5, pady=5)
        self.top_middle_frame.grid(row=0, column=2, rowspan=3, columnspan=4, padx=5, pady=5)
        self.top_right_side_frame.grid(row=0, column=6, rowspan=3, columnspan=2, padx=5, pady=5)

        self.bottom_frame.grid(row=3, column=2, rowspan=4, columnspan=4, padx=10, pady=10)

        # define/create widgets
        #

        # left side buttons
        self.lb1 = Button(self.top_left_side_frame, text="LB1", width=10)
        self.lb2 = Button(self.top_left_side_frame, text="LB2", width=10)
        self.lb3 = Button(self.top_left_side_frame, text="LB3", width=10)

        # middle frame label placeholders
        self.ml1 = Label(self.top_middle_frame, text="", height=2, width=10)
        self.ml2 = Label(self.top_middle_frame, text="", height=2, width=10)
        self.ml3 = Label(self.top_middle_frame, text="", height=2, width=10)
        self.ml4 = Label(self.top_middle_frame, text="", height=2, width=10)
        self.ml5 = Label(self.top_middle_frame, text="", height=2, width=10)
        self.ml6 = Label(self.top_middle_frame, text="", height=2, width=10)
        self.ml7 = Label(self.top_middle_frame, text="", height=2, width=10)
        self.ml8 = Label(self.top_middle_frame, text="", height=2, width=10)
        self.ml9 = Label(self.top_middle_frame, text="", height=2, width=10)
        self.ml10 = Label(self.top_middle_frame, text="", height=2, width=10)
        self.ml11 = Label(self.top_middle_frame, text="", height=2, width=10)
        self.ml12 = Label(self.top_middle_frame, text="", height=2, width=10)

        # other middle frame widgets
        self.mid_title_label = Label(self.top_middle_frame, text="Title", height=2)
        self.mid_title_input = Entry(self.top_middle_frame, width=20)
        
        self.mid_acc_info_title_label = Label(self.top_middle_frame, height=2)
        self.mid_acc_info_body_label = Label(self.top_middle_frame, height=2)

        self.rb1 = Button(self.top_right_side_frame, text="RB1", width=10)
        self.rb2 = Button(self.top_right_side_frame, text="RB2", width=10)
        self.rb3 = Button(self.top_right_side_frame, text="RB3", width=10)

        self.npb1 = Button(self.bottom_frame, text="1", width=5)
        self.npb2 = Button(self.bottom_frame, text="2", width=5)
        self.npb3 = Button(self.bottom_frame, text="3", width=5)
        self.npb4 = Button(self.bottom_frame, text="4", width=5)
        self.npb5 = Button(self.bottom_frame, text="5", width=5)
        self.npb6 = Button(self.bottom_frame, text="6", width=5)
        self.npb7 = Button(self.bottom_frame, text="7", width=5)
        self.npb8 = Button(self.bottom_frame, text="8", width=5)
        self.npb9 = Button(self.bottom_frame, text="9", width=5)
        self.npb10 = Button(self.bottom_frame, text="DEL", width=5)
        self.npb11 = Button(self.bottom_frame, text="0", width=5)
        self.npb12 = Button(self.bottom_frame, text="OK", width=5)

        # place widgets in window (ie use pack or grid or whatever layout manager to place widgets)
        self.lb1.grid(row=0, column=0, columnspan=2, sticky=E, padx=5, pady=5)
        self.lb2.grid(row=1, column=0, columnspan=2, sticky=E, padx=5, pady=5)
        self.lb3.grid(row=2, column=0, columnspan=2, sticky=E, padx=5, pady=5)

        self.display_blank_page()

        self.rb1.grid(row=0, column=0, columnspan=2, sticky=W, padx=5, pady=5)
        self.rb2.grid(row=1, column=0, columnspan=2, sticky=W, padx=5, pady=5)
        self.rb3.grid(row=2, column=0, columnspan=2, sticky=W, padx=5, pady=5)

        self.npb1.grid(row=0, column=0)
        self.npb2.grid(row=0, column=1)
        self.npb3.grid(row=0, column=3)
        self.npb4.grid(row=1, column=0)
        self.npb5.grid(row=1, column=1)
        self.npb6.grid(row=1, column=3)
        self.npb7.grid(row=2, column=0)
        self.npb8.grid(row=2, column=1)
        self.npb9.grid(row=2, column=3)
        self.npb10.grid(row=3, column=0)
        self.npb11.grid(row=3, column=1)
        self.npb12.grid(row=3, column=3)

    def render_card(self):
        self.display_entry_page("Enter Card Number")

    def render_pin(self):
        self.display_entry_page("Enter PIN", True)
        self.mid_title_input.configure(show='*')

    def render_selection(self, option1, option2, option3, option4, option5):
        self.display_options_page(lb1_lab=option1, lb2_lab=option2, lb3_lab="Cancel", rb1_lab=option3, rb2_lab=option4,
                                  rb3_lab=option5)
    
    def render_overview(self, acc_name, acc_type, acc_number):
        self.display_overview_page(acc_name, acc_type, acc_number)

    def render_balance(self, input_title, input_info, lb3_lab='', rb3_lab=''):
        self.display_info_page(input_title, input_info, lb3_lab, rb3_lab)
    
    def render_deposit(self):
        self.display_entry_page("Enter Deposit Amount", True, True)
        
    def render_withdraw(self):
        self.display_options_page(lb1_lab="$20", lb2_lab="$100", lb3_lab="Cancel", rb1_lab="$500", rb2_lab="Other",
                                  rb3_lab="Back")
        
    def render_cash(self):
        self.display_entry_page("Enter Custom Withdrawal Amount", True, True)

    def render_done(self):
        self.display_info_page('Done?', '', 'Yes', 'No')
        
    def render_error(self, error_msg):
        self.display_info_page('ERROR', error_msg, 'Cancel', 'Back')

    def clear_screen(self):
        self.mid_title_label.configure(text='')
        self.mid_title_input.configure(show='')
        self.mid_title_input.delete(0, END)
        self.mid_acc_info_title_label.configure(text='')
        self.mid_acc_info_body_label.configure(text='')

        self.ml1.configure(text='')
        self.ml2.configure(text='')
        self.ml3.configure(text='')
        self.ml4.configure(text='')
        self.ml5.configure(text='')
        self.ml6.configure(text='')
        self.ml7.configure(text='')
        self.ml8.configure(text='')
        self.ml9.configure(text='')
        self.ml10.configure(text='')
        self.ml11.configure(text='')
        self.ml12.configure(text='')

    def display_blank_page(self):
        self.clear_screen()

        self.mid_title_label.grid_forget()
        self.mid_title_input.grid_forget()
        self.mid_acc_info_title_label.grid_forget()
        self.mid_acc_info_body_label.grid_forget()
        self.ml1.grid(row=0, column=0)
        self.ml2.grid(row=0, column=1)
        self.ml3.grid(row=0, column=2)
        self.ml4.grid(row=0, column=3)
        self.ml5.grid(row=1, column=0)
        self.ml6.grid(row=1, column=1)
        self.ml7.grid(row=1, column=2)
        self.ml8.grid(row=1, column=3)
        self.ml9.grid(row=2, column=0)
        self.ml10.grid(row=2, column=1)
        self.ml11.grid(row=2, column=2)
        self.ml12.grid(row=2, column=3)
        
    def display_entry_page(self, title='', enable_cancel=False, enable_back=False):
        self.display_blank_page()

        self.ml1.grid_forget()
        self.ml2.grid_forget()
        self.ml3.grid_forget()
        self.ml4.grid_forget()
        self.mid_title_label.grid(row=0, column=0, columnspan=4)
        self.mid_title_label.configure(text=title, anchor=CENTER)

        self.ml6.grid_forget()
        self.ml7.grid_forget()
        self.mid_title_input.grid(row=1, column=1, columnspan=2)
        
        if enable_cancel:
            self.ml9.configure(text="Cancel")
            
        if enable_back:
            self.ml12.configure(text="Back")
            
    def display_options_page(self, lb1_lab='', lb2_lab='', lb3_lab='', rb1_lab='', rb2_lab='', rb3_lab=''):
        self.display_blank_page()
        
        self.ml1.configure(text=lb1_lab, anchor=W)
        self.ml5.configure(text=lb2_lab, anchor=W)
        self.ml9.configure(text=lb3_lab, anchor=W)
        
        self.ml4.configure(text=rb1_lab, anchor=W)
        self.ml8.configure(text=rb2_lab, anchor=W)
        self.ml12.configure(text=rb3_lab, anchor=W)
    
    def display_overview_page(self, input_name, input_type, input_number):
        self.display_blank_page()

        self.ml2.grid_forget()
        
        self.ml6.grid_forget()
        self.ml7.grid_forget()
        
        self.mid_acc_info_title_label.configure(text=input_name, anchor=W, justify=LEFT, compound=LEFT)
        self.mid_acc_info_title_label.grid(row=0, column=1, columnspan=1, sticky=W)
        
        self.ml3.configure(text=input_number)
        
        self.mid_acc_info_body_label.configure(text=input_type, anchor=E, justify=LEFT, compound=LEFT)
        self.mid_acc_info_body_label.grid(row=1, column=1, columnspan=2, sticky=W)
        
        self.ml1.configure(text="Balance")
        self.ml9.configure(text="Cancel")
        
        self.ml4.configure(text="Withdraw")
        self.ml8.configure(text="Deposit")
        self.ml12.configure(text="Back")
        
    def display_info_page(self, input_title, input_info, lb3_lab='', rb3_lab=''):
        self.display_blank_page()
        
        self.ml1.grid_forget()
        self.ml2.grid_forget()
        self.ml3.grid_forget()
        self.ml4.grid_forget()
        
        self.mid_title_label.grid(row=0, column=0, columnspan=4)
        self.mid_title_label.configure(text=input_title)
        
        self.ml5.grid_forget()
        self.ml6.grid_forget()
        self.ml7.grid_forget()
        self.ml8.grid_forget()

        self.mid_acc_info_body_label.grid(row=1, column=0, columnspan=4)
        self.mid_acc_info_body_label.configure(text=input_info)
        
        self.ml9.configure(text=lb3_lab)
        self.ml12.configure(text=rb3_lab)

class TestController:
    _PAGE_NUMBER = 1

    def __init__(self):
        self.root = Tk()
        self.view = View(self.root)

        # bind events/callbacks
        self.view.npb12.configure(command=self.cycle)

    def cycle(self):

        curr_page = self._PAGE_NUMBER
        if curr_page == 1:
            self.view.master.title('Enter Card Page')
            self.view.render_card()
        elif curr_page == 2:
            self.view.master.title('Enter PIN')
            self.view.render_pin()
        elif curr_page == 3:
            self.view.master.title('Selection an Account')
            self.view.render_selection('Account1', 'Account2', 'Account3', 'Account4', 'Other')
        
        elif curr_page == 4:
            self.view.master.title('Selection a Transaction')
            self.view.render_overview("User's Chequing Account", "Type: Chequing Account", "1456874135")
            
        elif curr_page == 5:
            self.view.master.title('Account Balance')
            self.view.render_balance("Current Account Balance", "$5.00", "", "Back")
            
        elif curr_page == 6:
            self.view.master.title('Deposit')
            self.view.render_deposit()
            
        elif curr_page == 7:
            self.view.master.title('Withdraw')
            self.view.render_withdraw()
        
        elif curr_page == 8:
            self.view.master.title('Done Page')
            self.view.render_balance("Done?", "", "Yes", "No")
        
        self._PAGE_NUMBER += 1
        if self._PAGE_NUMBER > 8:
            self._PAGE_NUMBER = 1


if __name__ == "__main__":
    test = TestController()
    test.cycle()
    mainloop()
