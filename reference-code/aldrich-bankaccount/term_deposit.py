class TermDeposit:
    def __init__(self, input_term, input_amount):
        """
            Constructor for creating an instance of the class TermDeposit.
            
        Args:
            input_term: Duration of the term
            input_amount:   Amount held within the TermDeposit
        """
        
        self.remaining_term = input_term
        self.deposit_amount = input_amount

    def update_term(self):
        """
            Updates the term (decrements by 1). Returns True or False depending on whether the TermDeposit has reached
            the end of the term or not.
            
        Returns:
            Boolean
        """
        
        result = False
        if self.remaining_term > 1:
            self.remaining_term -= 1
        else:
            result = True

        return result

    @property
    def term(self):
        """
            Returns the remaining term of the TermDeposit
            
        Returns:
            Int representing the remaining term of the TermDeposit
        """
        
        return self.remaining_term

    @property
    def term_deposit(self):
        """
            Return the amount of funds held within the TermDeposit
            
        Returns:
            Number representing the funds held within the TermDeposit
        """
        
        return self.deposit_amount


def test():
    """
        Test function for testing the functionality of the class TermDeposit
        
    Returns:
        Nothing
    """
    test_term = TermDeposit(18, 5000)
    print(test_term.term_deposit)
    for x in range(18):
        print("%d: %s" % (17 - x, test_term.update_term()))


if __name__ == "__main__":
    test()