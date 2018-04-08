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
        print('\nMain menu: ')
        return input('\n1. Manage existing customer\n2. Create new customer\n3. Back\n4. Quit')

    def showAccMenu(self):
        return input('\n1. Manage account\n2. Open new account\n3. Back\n4. Quit')

    def getAccNum(self):
        return input('Enter account number: ')

    def showManAccMenu(self):
        return input('\n1. Deposit\n2. Withdraw\n3. Balance\n4. Charge fee\n5. Back\n6. Quit\n')

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

    def getPIN(self):
        return input('Enter your PIN: ')

    def confirmPIN(self):
        return input('Confirm PIN: ')

    def printReport(self, report_content):
        print()
        print('{0:^65}'.format('----- Beginning of Report -----\n'))
        for item in report_content:
            print(item[0])
            print()
            for x in range(1, len(item)):
                print(item[x])
            print()
        print('{0:^65}'.format('----- End of Report -----'))



