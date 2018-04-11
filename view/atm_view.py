# atm_view.py
#
# ATM MVC program
#
# Team alroda
#
# Aldrich Huamg A01026502 2B
# Robert Janzen A01029341 2B
# David Xiao A00725026 2B

from tkinter import *

class View:
    def __init__(self, master):
        # create any instances of other support classes that are needed and save them
        # as attributes of this window
        self.master = master

        # set main window attributes such as title, geometry etc
        self.master.title('ATM')
        self.master.geometry('1015x500')
        self.master.configure(background='grey')

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

        # left side buttons
        self.lb1 = Button(self.top_left_side_frame, text="LB1", width=25, height=4)
        self.lb2 = Button(self.top_left_side_frame, text="LB2", width=25, height=4)
        self.lb3 = Button(self.top_left_side_frame, text="LB3", width=25, height=4)

        # middle frame label placeholders
        self.ml1 = Label(self.top_middle_frame, text="", height=5, width=20)
        self.ml2 = Label(self.top_middle_frame, text="", height=5, width=20)
        self.ml3 = Label(self.top_middle_frame, text="", height=5, width=20)
        self.ml4 = Label(self.top_middle_frame, text="", height=5, width=20)
        self.ml5 = Label(self.top_middle_frame, text="", height=5, width=20)
        self.ml6 = Label(self.top_middle_frame, text="", height=5, width=20)
        self.ml7 = Label(self.top_middle_frame, text="", height=5, width=20)
        self.ml8 = Label(self.top_middle_frame, text="", height=5, width=20)
        self.ml9 = Label(self.top_middle_frame, text="", height=5, width=20)
        self.ml10 = Label(self.top_middle_frame, text="", height=5, width=20)
        self.ml11 = Label(self.top_middle_frame, text="", height=5, width=20)
        self.ml12 = Label(self.top_middle_frame, text="", height=5, width=20)

        # other middle frame widgets
        self.mid_title_label = Label(self.top_middle_frame, text="Title", height=5, font=("Helvetica", 9))
        self.mid_title_input = Entry(self.top_middle_frame, width=48)
        
        self.mid_acc_info_title_label = Label(self.top_middle_frame, height=5)
        self.mid_acc_info_body_label = Label(self.top_middle_frame, height=5)

        self.rb1 = Button(self.top_right_side_frame, text="RB1", width=25, height=4)
        self.rb2 = Button(self.top_right_side_frame, text="RB2", width=25, height=4)
        self.rb3 = Button(self.top_right_side_frame, text="RB3", width=25, height=4)

        self.npb1 = Button(self.bottom_frame, text="1", width=10, height=3)
        self.npb2 = Button(self.bottom_frame, text="2", width=10, height=3)
        self.npb3 = Button(self.bottom_frame, text="3", width=10, height=3)
        self.npb4 = Button(self.bottom_frame, text="4", width=10, height=3)
        self.npb5 = Button(self.bottom_frame, text="5", width=10, height=3)
        self.npb6 = Button(self.bottom_frame, text="6", width=10, height=3)
        self.npb7 = Button(self.bottom_frame, text="7", width=10, height=3)
        self.npb8 = Button(self.bottom_frame, text="8", width=10, height=3)
        self.npb9 = Button(self.bottom_frame, text="9", width=10, height=3)
        self.npb10 = Button(self.bottom_frame, text="DEL", width=10, height=3)
        self.npb11 = Button(self.bottom_frame, text="0", width=10, height=3)
        self.npb12 = Button(self.bottom_frame, text="OK", width=10, height=3)

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
        """
            Render the card number entry page
        
        Returns:
            None
        """
        
        self.display_entry_page("Enter Card Number")

    def render_pin(self):
        """
            Renders the PIN entry page
        Returns:
            None
        """
        
        self.display_entry_page("Enter PIN", True)
        self.mid_title_input.configure(show='*')

    def render_selection(self, option1, option2, option3, option4, option5):
        """
            Renders the Selection page, which allows users to select which account to use for transactions
            
        Args:
            option1:
                String containing name of an account, empty string if not applicable
            option2:
                String containing name of an account, empty string if not applicable
            option3:
                String containing name of an account, empty string if not applicable
            option4:
                String containing name of an account, empty string if not applicable
            option5:
                String containing name of an account, empty string if not applicable

        Returns:
            None
        """
        
        self.display_options_page(lb1_lab=option1, lb2_lab=option2, lb3_lab="Cancel", rb1_lab=option3, rb2_lab=option4,
                                  rb3_lab=option5)
    
    def render_overview(self, acc_name, acc_type, acc_number):
        """
            Renders the account overview page
            
        Args:
            acc_name:
                String containing the name of the account
            acc_type:
                String containing the type of the account
            acc_number:
                String containing the account number

        Returns:
            None
        """
        
        self.display_overview_page(acc_name, acc_type, acc_number)

    def render_balance(self, input_title, input_info, lb3_lab='', rb3_lab=''):
        """
            Renders the balance page which displays the current balance of the account
            
        Args:
            input_title:
                String containing the title of the page
            input_info:
                String containing the information to be displayed
            lb3_lab:
                String that represents the functionality of left button 3
            rb3_lab:
                String that represents the functionality of right button 3

        Returns:
            None
        """
        
        self.display_info_page(input_title, input_info, lb3_lab, rb3_lab)
    
    def render_deposit(self):
        """
            Renders the deposit page
            
        Returns:
            None
        """
        
        self.display_entry_page("Enter Deposit Amount", True, True)
        
    def render_withdraw(self):
        """
            Renders the withdraw page
            
        Returns:
            None
        """
        
        self.display_options_page(lb1_lab="$20", lb2_lab="$100", lb3_lab="Cancel", rb1_lab="$500", rb2_lab="Other",
                                  rb3_lab="Back")
        
    def render_cash(self):
        """
            Renders the custom withdraw amount entry page
            
        Returns:
            None
        """
        
        self.display_entry_page("Enter Custom Withdrawal Amount", True, True)

    def render_done(self):
        """
            Renders the done page
            
        Returns:
            None
        """
        
        self.display_info_page('Done?', '', 'Yes', 'No')
        
    def render_error(self, error_msg):
        """
            Renders the error page
        Args:
            error_msg:
                String the contains the error message

        Returns:
            None
        """
        if error_msg == "Account Not Found":
            self.display_info_page('ERROR', error_msg, 'Cancel')
            
        else:
            self.display_info_page('ERROR', error_msg, 'Cancel', 'Back')
    
    def render_withdrawal_confirmation(self, input_amount):
        """
            Renders the screen for withdrawal confirmation
        Args:
            input_amount:
                Amount that was withdrawn
        Returns:
            None
        """
        message = 'Withdrawn ${0:.2f}, please take out the cash from bellow.'.format(round(float(input_amount), 2))
        self.display_info_page('Notice', message, '', 'Continue')
        

    def clear_screen(self):
        """
            Clears the contents of the view
            
        Returns:
            None
        """
        
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
        """
            Renders a blank page
            
        Returns:
            None
        """
        
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
        """
            Configures widgets to display an entry page. The entry page mainly consists of a title label at the top,
            and an entry widget at the middly.
            
        Args:
            title:
                String containing the title of the page
            enable_cancel:
                Boolean that enable the Cancel function
            enable_back:
                Boolean that enables the Back function

        Returns:
            None
        """
        
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
        """
            Configures widgets to display an options page. The options page mainly consists of widgets on the left and
            right side with lables that describes the function that the side buttons have
            
        Args:
            lb1_lab:
                String that describes function of the corresponding side button, empty string for no function
            lb2_lab:
                String that describes function of the corresponding side button, empty string for no function
            lb3_lab:
                String that describes function of the corresponding side button, empty string for no function
            rb1_lab:
                String that describes function of the corresponding side button, empty string for no function
            rb2_lab:
                String that describes function of the corresponding side button, empty string for no function
            rb3_lab:
                String that describes function of the corresponding side button, empty string for no function

        Returns:
            None
        """
        
        self.display_blank_page()
        
        self.ml1.configure(text=lb1_lab, anchor=W)
        self.ml5.configure(text=lb2_lab, anchor=W)
        self.ml9.configure(text=lb3_lab, anchor=W)
        
        self.ml4.configure(text=rb1_lab, anchor=E)
        self.ml8.configure(text=rb2_lab, anchor=E)
        self.ml12.configure(text=rb3_lab, anchor=E)
    
    def display_overview_page(self, input_name, input_type, input_number):
        """
            Configures widgets to display the account overview page
            
        Args:
            input_name:
                String containing the account name
            input_type:
                String containing the account type
            input_number:
                String containing the account number

        Returns:
            None
        """
        
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
        """
            Configures widgets to display an information page. The info consists of a title and a middle text label
            
        Args:
            input_title:
                String containing the title of the page
            input_info:
                String containing the information to be displayed on the page
            lb3_lab:
                String describing the function of the left button 3
            rb3_lab:
                String describing the function of the right button 3

        Returns:
            None
        """
        
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

if __name__ == "__main__":
    print('atm_view.py')
