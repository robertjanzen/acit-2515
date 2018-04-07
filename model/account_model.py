class Account():

    _NEXT_ACCT_NUM = 10000

    def __init__(self, accName, balance=0):
        """constructor for the super class"""
        self.accNum = Account._NEXT_ACCT_NUM
        Account._NEXT_ACCT_NUM += 1
        self.accName = accName
        if self.check_float(balance):
            self._balance = balance
        # self.logObj = Translog()
        # self.log = self.logObj.list
        # self.add_entry('deposit', balance)

    def change_name(self, accName):
        """changes owner name"""
        self.accName = accName

    def withdraw(self, amount):
        """allow withdraw if valid amount and sufficient balance, print error message otherwise"""
        if self.check_float(amount):
            if self._balance >= amount:
                self._balance -= amount
                # self.add_entry('withdraw', amount)
            else:
                print('Insufficient funds.')

    def deposit(self, amount):
        """allow deposit if valid amount"""
        if self.check_float(amount):
            self._balance += amount
            # self.add_entry('deposit', amount)

    def get_balance(self):
        """print out the current balance"""
        print(self._balance)

    # def add_entry(self, type, amount):
    #     """add transaction information to the log"""
        # self.logObj.add_entry(self.accNum, type, amount)

    # def show_transaction(self):
    #     """show all lines in the transaction log for an acccount"""
    #     print(self.__str__())
    #     for i in self.log:
    #         print(i)

    def check_float(self, value):
        """this function first checks if the value can be made into a float
        then check to see if the value is greater than or equal to 0
        returns false if both criteria are not met so account information is not changed"""
        try:
            float(value)
            if value >= 0:
                return True
            else:
                print('Invalid value, please re-enter amount.')
                return False
        except ValueError:
            print('Invalid value, please re-enter amount.')
            return False

    @property
    def balance(self):
        return self._balance



if __name__ == '__main__':
    a = Account('david', 500000)
    a.deposit(200000.01)
    a.withdraw(12.5)
    print(a.balance)
    # a.show_transaction()