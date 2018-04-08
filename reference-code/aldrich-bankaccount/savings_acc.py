from account import Account
from constants import *


class Savings(Account):
    __MIN_BALANCE = SAVINGS_BALANCE_MIN_LIMIT
    __LOW_BALANCE_FEE = LOW_BALANCE_FEE
    __ACC_INTEREST = GOOD_STANDING_INTEREST
    
    def __init__(self, user_name=DEFAULT_ACC_NAME, input_balance=DEFAULT_ACC_MIN_BALANCE):
        """
            Constructor for creating a new instance of the class Savings. First checks if the input account balance at
            least meets the balance limit before creating the account.
            
        Args:
            user_name:  Name of the account holder
            input_balance:  Initial balance of the account
        """
        
        if self.check_float(input_balance):
            if input_balance < SAVINGS_BALANCE_MIN_LIMIT:
                print("Not enough balance to create savings account...")
                exit(2)
                
        else:
            print("Please enter valid number of account balance...")
            exit(1)
        super().__init__(user_name, input_balance)
        self.standing = True
        self.type = "Savings"

    def check_standing(self):
        """
            Checks to see if the account balance is great than or equal to the saving balance minimum limit. If it is,
            then account is in good standing.
            
        Returns:
            Boolean representing result of the check
        """
        
        return self.balance >= Savings.__MIN_BALANCE

    def withdraw(self, input_amount):
        """
            Savings version of withdraw. Calls the withdraw method of the parent class, then checks to see if account
            standing has changed from good to bad. If account standing did change for the worse, apply the low balance
            fee to the account.
            
        Args:
            input_amount:   Amount to be withdrawn from the account

        Returns:
            Nothing
        """
        
        original_standing = self.standing
        super().withdraw(input_amount)
        self.standing = self.check_standing()
        if not self.standing:
            if original_standing:
                self.charge_low_balance_fee()

    def deposit(self, input_amount):
        """
            Savings version of deposit. Calls the deposit method the parent class, then updates the account standing.
            
        Args:
            input_amount:   Amount to be deposited to the account

        Returns:
            Nothing
        """
        
        super().deposit(input_amount)
        self.standing = self.check_standing()
        
    def charge_low_balance_fee(self):
        """
            Apply low balance fee to the account if account balance falls below the minimum savings balance limit.
            
        Returns:
            Nothing
        """
        
        if self.balance < Savings.__MIN_BALANCE:
            self.add_fee(Savings.__LOW_BALANCE_FEE)
    
    def pay_interest(self):
        """
            Checks to see if account is in good standing, if it is pays interest to the account.
            
        Returns:
            Nothing
        """
        
        if self.balance > Savings.__MIN_BALANCE:
            paid_interest = self.balance * Savings.__ACC_INTEREST
            self.acc_balance += paid_interest
            self.transactions.update_log("Pay-Interest", "$%.2f" % paid_interest)
            self.standing = self.check_standing()
    
    
def test():
    """
        Function for testing the functionality of the class Savings
        
    Returns:
        Nothing
    """
    
    test_acc1 = Savings("bob", 1000)
    print(test_acc1)

    test_acc1.withdraw('s')
    test_acc1.withdraw(23)
    test_acc1.withdraw(5)
    test_acc1.deposit('1001')
    test_acc1.withdraw(1001)
    test_acc1.change_name("Albert Smith")
    test_acc1.pay_interest()
    test_acc1.deposit(5000)
    test_acc1.pay_interest()

    print(test_acc1.show_transactions())
    print(test_acc1)


if __name__ == "__main__":
    test()
