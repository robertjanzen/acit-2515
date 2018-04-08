from transaction_log import TransactionLog
from fee import Fee
from constants import *


class Account:
    __NEXT_ACCT_NUM = DEFAULT_STARTING_ACC_ID

    def __init__(self, user_name=DEFAULT_ACC_NAME, account_balance=DEFAULT_ACC_MIN_BALANCE):
        """
            Constructor for creating an instance of the class Account. Creates an instance of the class TransactionLog,
            and an instance of the class Fee as instance attributes.
            
        Args:
            user_name:  Name of the account holder
                
            account_balance:    Initial balance of the account
        """
        
        if not self.check_float(account_balance):
            exit(1)
        elif float(account_balance) < DEFAULT_ACC_MIN_BALANCE:
            print("Please enter a valid account starting balance...")
            exit(2)
        
        self.acc_balance = float(account_balance)
        self.name = str(user_name)
        self.acc_num = Account.__NEXT_ACCT_NUM
        self.transactions = TransactionLog(self.acc_num)
        self.balance_limit = DEFAULT_ACC_MIN_BALANCE
        self.transactions.update_log("Account-Created", "$%.2f" % self.acc_balance)
        self.fees = Fee(self.acc_num)
        self.type = "Normal Account"
        
        Account.update_next_acct_num()
        
    def withdraw(self, input_amount):
        """
            Checks the input_amount to make sure that it can be converted to a float and is a positive number. Then
            subtracts the input_amount from the instance attribute self.acc_balance.
            
        Args:
            input_amount:   Amount to be withdrawn from the account.

        Returns:
            Nothing
        """
        
        if not self.check_float(input_amount):
            return
        
        amount = float(input_amount)
        
        if amount >= 0:
            if self.acc_balance - amount < self.balance_limit:
                print("Insufficient funds...")
                
            else:
                self.acc_balance -= amount
                self.transactions.update_log("Withdrawal", "$%.2f" % amount)
            
        else:
            print("Account not updated, please enter a positive number...")
            
    def deposit(self, input_amount):
        """
            Checks the input_amount to make sure that it can be converted to a float and is a positive number. Then
            adds the input_amount to the instance attribute self.acc_balance.
            
        Args:
            input_amount:   Amount to be deposited to account balance

        Returns:
            Nothing
        """
        
        if not self.check_float(input_amount):
            return
    
        amount = float(input_amount)
        
        if amount >= 0:
            self.acc_balance += amount
            self.transactions.update_log("Deposit", "$%.2f" % amount)
        else:
            print("Account not updated, please enter a positive number...")

    def change_name(self, new_name):
        """
            Changes the name of the account holder
            
        Args:
            new_name:   Name to change the account holder's name to

        Returns:
            Nothing
        """
        
        self.name = str(new_name)
        self.transactions.update_log("Name-Changed-To", new_name)
        
    def show_transactions(self):
        """
            Returns a formatted string containing the full recorded transaction log of the account.
            
        Returns:
            Formatted string of the recorded transaction log of the account.
        """
        
        return self.transactions.get_log()
    
    def add_fee(self, input_amount, input_multiplier=DEFAULT_FEE_MULTIPLIER):
        """
            Adds a new fee entry to the account
            
        Args:
            input_amount: Amount of the fee
            input_multiplier: Multiplier to be applied to the fee

        Returns:
            Nothing
        """
        
        if not self.check_float(input_amount):
            return
    
        amount = float(input_amount)
    
        if amount >= 0:
            self.fees.add_fee(input_amount, input_multiplier)
            self.transactions.update_log("Add-Fee", "$%.2f" % amount)
    
        else:
            print("Account not updated, please enter a positive number...")
    
    def charge_fee(self):
        """
            Charges the account with all the fee entries stored in the instance attribute self.fees.
            
        Returns:
            Nothing
        """
        
        charge_amt = self.fees.charge_all()
        if charge_amt <= 0:
            return
        self.acc_balance -= charge_amt
        self.transactions.update_log("Charged-Fee", "$%.2f" % charge_amt)
    
    def acc_info(self):
        """
            Returns a formatted string containing the basic account information.
            
        Returns:
            Formatted string containing the basic account information
        """
        
        return "\nAccount Holder: %s\nAccount Number: %s\nAccount Balance: $%.2f\nAccount Type: %s" % \
                 (self.name, self.acc_num, self.acc_balance, self.type)
    
    def __str__(self):
        """
            Prints the account information.
            
        Returns:
            String containing the basic account information.
        """
        
        return self.acc_info()
    
    @staticmethod
    def check_float(input_amount):
        """
            Checks to see if the input can be converted to float. Returns True if possible, False if not possible.
            
        Args:
            input_amount:   Value to be checked

        Returns:
            Boolean value
        """
        
        try:
            float(input_amount)
        except:
            print("Please enter a valid amount, expecting a number...")
            return False
        
        return True
    
    @property
    def balance(self):
        """
            Returns account balance.
            
        Returns:
            Account balance.
        """
        
        return self.acc_balance
    
    @classmethod
    def update_next_acct_num(cls):
        """
            Automatically increments the class attribute __NEXT_ACCT_NUM to create a new unique account number for the
            next instance of the class Account to be created.
            
        Returns:
            Nothing
        """
        
        cls.__NEXT_ACCT_NUM += ACC_ID_INCREMENT_VALUE


def test():
    """
        Tests the attributes and methods of the Account class.
        
    Returns:
        Nothing
    """
    
    test_acc1 = Account("test", 10)
    print(test_acc1)
    
    test_acc2 = Account("test", 102)
    
    test_acc1.withdraw('s')
    test_acc1.withdraw(23)
    test_acc1.withdraw(5)
    test_acc1.deposit('21')
    test_acc1.change_name("Albert Smith")

    print(test_acc1)
    print(test_acc1.show_transactions())
    
    test_acc2.change_name("Smith Smithson")
    test_acc2.deposit(25.22)
    test_acc2.withdraw(-23)
    test_acc2.withdraw('-23')
    test_acc2.withdraw(23.50)
    test_acc2.deposit(-22)
    test_acc2.deposit("six dollars")
    print("Account balance for test_acc2: $%.2f" % test_acc2.balance)
    print(test_acc2)
    print(test_acc2.show_transactions())

    test_acc3 = Account("test", "smith")
    test_acc3 = Account(account_balance=76.50)
    
    print(test_acc3)
    print(test_acc3.show_transactions())
    
    test_acc4 = Account(account_balance=100)
    print(test_acc4)
    
    test_acc4.charge_fee()
    print(test_acc4.show_transactions())
    test_acc4.add_fee(10,2)
    test_acc4.add_fee(2)
    test_acc4.add_fee(23,0.15)
    print(test_acc4.show_transactions())
    print(test_acc4)
    test_acc4.charge_fee()
    print(test_acc4)
    print(test_acc4.show_transactions())
    
    
if __name__ == "__main__":
    test()
