class Fee:
    def __init__(self, account_number):
        """
            Constructor for creating a new instance of the class Fee. Contains instance attribute self.fee which
            contains a list of outstanding fees tied to the account.
        """
        
        self.outstanding_fee = []
        self.acc_num = account_number
        
    def add_fee(self, base_amt, input_multiplier=1.0):
        """
            Checks to see if both input parameters can be converted into float, then calculates and add fee into the
            instance attribute self.oustanding_fee
            
        Args:
            base_amt:   Base fee charge
            input_multiplier:   Multiplier to be applied to the base fee charge

        Returns:
            Nothing
        """
        
        try:
            amount = float(base_amt)
            multiplier = float(input_multiplier)
            
        except:
            print("Invalid fee value, please enter a valid number...")
            return
            
        if amount < 0 or multiplier < 0:
            print("Please enter a positive number...")
            return
        
        new_outstanding_fee = round(amount * multiplier, 2)
        self.outstanding_fee.append(new_outstanding_fee)
        
    def display_fees(self):
        """
            Prints out a formatted string which lists all outstanding fees for the account.
            
        Returns:
            Nothing
        """
        
        display_string = "Outstanding fees:\n" + '\n'.join(("$%.2f" % entry)for entry in self.outstanding_fee)
        print(display_string)
    
    def charge_all(self):
        """
            Calculates the sum of all of the outstanding fees then clears the outstanding_fees list.
            
        Returns:
            Sum of all of the outstanding fees
        """
        
        subtotal = sum(self.outstanding_fee)
        self.outstanding_fee[:] = []
        return subtotal


def test():
    """
        Test function for testing the attributes and methods of the class Fee
        
    Returns:
        Nothing
    """
    
    test_fees = Fee(1)
    test_fees.add_fee(42.222)
    test_fees.add_fee(42, 1)
    test_fees.display_fees()
    charged_amt = test_fees.charge_all()
    test_fees.display_fees()
    print(charged_amt)
    test_fees.add_fee(-22)
    test_fees.add_fee("2t2")
    test_fees.display_fees()
    test_fees.add_fee(22, 0.98)
    test_fees.display_fees()


if __name__ == "__main__":
    test()