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
        return input('\n1. Manage existing customer\n2. Create new customer\n3. Quit\n')

    def showManUid(self):
        return input('\n1. Create new account\n2. Delete account\n3. View transaction report\n'
                     '4. Quit')

    def showAccMenu(self):
        return input('\n1. Manage account\n2. Open new account\n3. Quit\n')

    def accountType(self):
        return input('\n1. Create Chequing account\n2. Create saving account\n3. Quit\n')

    def getAccName(self):
        return input('Enter account holder name: ')

    def getInitialDeposit(self):
        return input('Enter initial deposit amount: ')

    def getManInput(self):
        return input('\n1. Deposit into an account\n2. Quit\n')

    def uidInput(self):
        return input('Enter the user ID: ')

    def accNumInput(self):
        return input('Enter the account number: ')

    def depositInput(self):
        return input('Enter deposit amount: ')

