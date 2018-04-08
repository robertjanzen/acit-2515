from account import Account
from cheq_account import Chequing
from savings_acc import Savings
from term_savings import TermSavings


class ManageAccount:
    def __init__(self):
        """
            Constructor for creating an instance of the class ManageAccount. The instance contains a list of created
            accounts.
        """
        
        self.accounts = []
    
    def create_account(self, name="New account holder", balance=0.0):
        """
            Creates and returns a new Account instance.
            
        Args:
            name:   Name of the account holder
            balance:    Initial account balance

        Returns:
            Newly created Account instance
        """
        
        if not self.check_num(balance):
            return
        
        new_account = Account(name, float(balance))
        self.accounts.append(new_account)
        return new_account
    
    def create_chequing_account(self, name="New account holder", balance=0.0):
        """
            Creates and returns a new Chequing instance.
           
        Args:
            name:   Name of the chequing account holder
            balance:    Initial chequing account balance

        Returns:
            Newly created Chequing instance
        """
        
        if not self.check_num(balance):
            return
        
        new_cheq_account = Chequing(name, float(balance))
        self.accounts.append(new_cheq_account)
        return new_cheq_account
    
    def create_savings_account(self, name="New account holder", balance=0.0):
        """
            Creates and returns a new Savings instance.
           
        Args:
            name:   Name of the savings account holder
            balance:    Initial savings account balance

        Returns:
            Newly created Savings instance
        """
        
        if not self.check_num(balance):
            return
        
        new_save_account = Savings(name, float(balance))
        self.accounts.append(new_save_account)
        return new_save_account
    
    def create_term_save_account(self, name="New account holder", balance=0.0):
        """
            Creates and returns a new TermSavings instance.
           
        Args:
            name:   Name of the term savings account holder
            balance:    Initial term savings account balance

        Returns:
            Newly created TermSavings instance
        """
        
        if not self.check_num(balance):
            return
        
        new_term_save_account = TermSavings(name, float(balance))
        self.accounts.append(new_term_save_account)
        return new_term_save_account
    
    def charge_all(self):
        """
            Charges all outstanding fees for all the accounts.
            
        Returns:
            Nothing
        """
        
        for account in self.accounts:
            account.charge_fee()
    
    def get_all_summary(self):
        """
            Creates and returns a formatted string containing the basic information of all accounts stored in the
            instance attribute self.accounts.
            
        Returns:
            Formatted string containing the basic information of all accounts stored in the instance attribute
            self.accounts
        """
        
        output = ""
        for account in self.accounts:
            output += account.acc_info() + '\n'
        return output
    
    def get_all_log(self):
        """
            Creates and returns a formatted string containing the transaction log of all accounts stored in the instance
            attribute self.accounts.
            
        Returns:
            Formatted string containing the transaction log of all accounts stored in the instance attribute
            self.accounts
        """
        
        output = ""
        for account in self.accounts:
            output += account.show_transactions() + '\n'
        return output
            
    @staticmethod
    def check_num(input_amount):
        """
            Checks to see if inputted variable can be converted to a float. Returns True if possible and False if not
            possible.
            
        Args:
            input_amount:   Variable to be checked

        Returns:
            Boolean
        """
        
        try:
            float(input_amount)
        except:
            return False
        
        return True


def main():
    """
        The main function.
        
    Returns:
        Nothing
    """
    
    account_manager = ManageAccount()
    
    sally_ch_acc = account_manager.create_chequing_account("Sally", 1000)
    joe_sav_acc = account_manager.create_savings_account("Joe", 5000)
    sally_term_sav_acc = account_manager.create_term_save_account("Sally", 7000)
    
    joe_sav_acc.deposit(100)
    print("Joe's saving account balance: $%.2f" % joe_sav_acc.balance)
    
    sally_ch_acc.withdraw(50)
    sally_term_sav_acc.withdraw(50)
    
    print("Sally's chequing account balance: $%.2f" % sally_ch_acc.balance)
    print("Sally's term savings account balance: $%.2f" % sally_term_sav_acc.balance)
    
    sally_ch_acc.withdraw(500)
    sally_ch_acc.withdraw(500)

    account_manager.charge_all()
    
    # Only the two savings account have paid interest
    joe_sav_acc.pay_interest()
    sally_term_sav_acc.pay_interest()
    
    joe_sav_acc.change_name("Joseph")
    
    print(account_manager.get_all_summary())
    
    print(account_manager.get_all_log())
    
    
if __name__ == "__main__":
    main()
