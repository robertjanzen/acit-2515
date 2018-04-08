# This presents the CLI view for bank employees
# import getpass

class CLIView:

    def __init__(self):
        # self.getp = getpass.getpass
        pass

    def getCLIName(self):
        user_name = input('Enter your username: ')
        return user_name

    def getCLIPwd(self):
        # password = getp('Enter your password: ')
        password = input('Enter your password: ')
        return password

    def showUidMenu(self):
        print('Main menu: ')
        return input('\n1. Manage existing customer\n2. Create new customer\n3. Quit\n')

    def showAccMenu(self):
        return input('\n1. Manage account\n2. Open new account\n3. Quit\n')

    def getAccNum(self):
        return input('Enter account number: ')

    def showManAccMenu(self):
        return input('\n1. Deposit\n2. Withdraw\n3. Balance\n4. Charge fee\n5. Quit\n')

    def getAccType(self):
        return input('\n1. Chequing\n2. Saving\n3. Quit\n')

    def getAccName(self):
        return input('Enter account name: ')

    def getDeposit(self):
        return input('Enter deposit amount: ')

    def getWithdraw(self):
        return input('Enter withdraw amount: ')

    def getUid(self):
        return input('Enter the user ID: ')

    def showBalance(self, balance):
        print('The current balance is: ', balance)



