from savings_acc import Savings
from term_deposit import TermDeposit
from constants import *


class TermSavings(Savings):
    __TERM_DURATION = DEFAULT_TERM
    
    def __init__(self, input_name=DEFAULT_ACC_NAME, input_balance=DEFAULT_ACC_MIN_BALANCE, input_term=__TERM_DURATION):
        """
            Constructor for creating a new instance of the class TermSavings. This class contains a list of TermDeposit
            objects as one of its instance attributes.
            
        Args:
            input_name: Name of the account holder
            input_balance:  Initial balance of the account
            input_term: Term of the deposit of the account
        """
        
        super().__init__(input_name, input_balance)
        self.term_deposits = []
        self.default_term = input_term
        self.available_funds = INITIAL_AVAILABLE_FUNDS
        self.create_new_term_deposit(input_balance)
        self.type = "Term Savings"
        
    def update_term(self):
        """
            Update all term deposits for the account, advances all terms by one day. If a deposit's term is up, the
            funds held within the deposit is allocated as part of the account's available funds.
            
        Returns:
            Nothing
        """
        
        marked_deposits = []
        for entry in self.term_deposits:
            if entry.update_term():
                self.available_funds += entry.term_deposit
                self.transactions.update_log("Deposit-Matured", "$%.2f" % entry.term_deposit)
                marked_deposits.append(entry)
        for deposits in marked_deposits:
            self.term_deposits.remove(deposits)
                
    def create_new_term_deposit(self, input_amount):
        """
            Creates a new TermDeposit object for the class.
            
        Args:
            input_amount:   Amount to be deposited as TermDeposit for the account

        Returns:
            nothing
        """
        new_term_deposit = TermDeposit(self.default_term, input_amount)
        self.term_deposits.append(new_term_deposit)

    def deposit(self, input_amount):
        """
            TermSavings version of deposit. Deposits funds as term deposits instead of normal deposits.
            
        Args:
            input_amount:   Amount to be deposited to the account

        Returns:
            Nothing
        """
        
        if not self.check_float(input_amount):
            return
        
        amount = float(input_amount)
        
        if amount >= 0:
            self.create_new_term_deposit(amount)
            super().deposit(amount)
        else:
            print("Account not updated, please enter a positive number...")

    def withdraw(self, input_amount):
        """
            TermSavings version of withdraw. Checks if available funds is enough to withdraw the withdraw amount. Only
            allows withdrawal if there is enough available funds in the account.
            
        Args:
            input_amount:   Amount to be withdrawn from the account

        Returns:
            Nothing
        """
        
        if not self.check_float(input_amount):
            return

        amount = float(input_amount)

        if amount >= 0:
            if amount <= self.available_funds:
                super().withdraw(amount)
                self.available_funds -= amount
            else:
                print("Insufficient funds...")
    
    def acc_info(self):
        output = super().acc_info() + "\nAvailable Funds: $%.2f" % self.available_funds
        return output

    def __str__(self):
        """
            Returns a formatted string containing the basic information of the account, including the available funds
            of the account.
            
        Returns:
            Formatted string of account basic information
        """
        
        return self.acc_info()
        
        
def test():
    """
        Test function for testing the functionality of the class TermSavings
        
    Returns:
        Nothing
    """
    
    test_acc1 = TermSavings("Perry", 1000000000)
    test_acc1.withdraw(500)
    print(test_acc1)
    for x in range(30):
        test_acc1.update_term()
    test_acc1.deposit(500)
    for x in range(30):
        test_acc1.update_term()
    print(test_acc1)
    test_acc1.withdraw(200)
    print(test_acc1)
    for x in range(30):
        test_acc1.update_term()
    print(test_acc1)
    print(test_acc1.show_transactions())


if __name__ == "__main__":
    test()
