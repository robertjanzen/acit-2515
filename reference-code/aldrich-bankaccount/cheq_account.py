from account import Account
from constants import *


class Chequing(Account):
    __OVERDRAFT_LIMIT = CHEQUING_OVERDRAFT_LIMIT
    __CHARGE_INTEREST = CHEQUING_INTEREST_CHARGE
    __BOUNCE_PENALTY = CHEQUING_BOUNCE_PENALTY
    
    def __init__(self, input_name=DEFAULT_ACC_NAME, input_balance=DEFAULT_ACC_MIN_BALANCE):
        """
            Constructor for creating a new instance of the class Chequing. This is a subclass of the parent class
            Account.
            
        Args:
            input_name: Name of the account holder
            input_balance:  Initial balance of the account
        """
        
        super().__init__(input_name, input_balance)
        self.balance_limit = Chequing.__OVERDRAFT_LIMIT
        self.type = "Chequing"

    def post_cheque(self, input_amount):
        """
            Posts a cheque for the chequing account. Cheque is bounced if it exceeds the overdraft limit. Overdraft
            interest is charged if account dips into overdraft range.(less than 0 but more than overdraft limit)
            
            
        Args:
            input_amount:   Amount on the cheque to be posted

        Returns:
            Nothing
        """
        
        try:
            amount = float(input_amount)
    
        except:
            print("Please enter a valid amount, expecting a number...")
            return

        penalty = 0
        success = True
    
        if amount >= 0:
            if (self.balance - amount) < Chequing.__OVERDRAFT_LIMIT:
                print("Insufficient funds, cheque bounced...")
                penalty = Chequing.__BOUNCE_PENALTY
                success = False
        
            else:
                self.acc_balance -= amount
                self.transactions.update_log("Post-Cheque", "$%.2f" % amount)
                self.charge_interest(amount)
                
            if not success:
                self.add_fee(penalty)
    
        else:
            print("Account not updated, please enter a positive number...")

    def withdraw(self, input_amount):
        """
            Withdraws from the account. Charges overdraft interest when account balance dips into overdraft range.
            (less than 0 and greater than overdraft limit)
            
        Args:
            input_amount:   Amount to be withdrawn

        Returns:
            Nothing
        """
        
        original_balance = self.balance
        super().withdraw(input_amount)
        if original_balance != self.balance:
            self.charge_interest(input_amount)

    def charge_interest(self, input_amount):
        """
            Calculates and charge overdraft interest based on overdraft amount if account balance falls within overdraft
            territory.
            
        Args:
            input_amount:   Most recent account balance withdrawn amount.

        Returns:
            Nothing
        """
        
        overdraft_amt = min(0 - self.acc_balance, input_amount)
        if overdraft_amt > 0:
            charged_interest = overdraft_amt * Chequing.__CHARGE_INTEREST
            self.acc_balance -= charged_interest
            self.transactions.update_log("Interest-Charge-for", "$%.2f" % charged_interest)
            

def test():
    """
        Test function for testing the attributes and methods of the class Chequing
        
    Returns:
        Nothing
    """
    
    test_acc1 = Chequing()
    print(test_acc1)
    
    test_acc1.withdraw('s')
    test_acc1.withdraw(23)
    test_acc1.withdraw(5)
    test_acc1.deposit('21')
    test_acc1.change_name("Albert Smith")
    test_acc1.post_cheque(25)
    test_acc1.withdraw(1000)

    test_acc1.post_cheque(1)
    test_acc1.post_cheque(5000)
    test_acc1.charge_fee()
    print(test_acc1)
    print(test_acc1.show_transactions())
    
    test_acc2 = Chequing(input_balance = 5000)
    test_acc2.withdraw(200)
    test_acc2.post_cheque(200)
    print(test_acc2)
    print(test_acc2.show_transactions())
    
    test_acc3 = Chequing("bob", "two hundred")
    test_acc3 = Chequing("bob", "200")
    test_acc3.withdraw("two hundred")
    test_acc3.post_cheque("one hundred")
    print(test_acc3)
    print(test_acc3.show_transactions())
    

if __name__ == "__main__":
    test()
