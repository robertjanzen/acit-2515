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
        return input('\n1. Manage existing customer\n2. Create new customer\n3. Pay interest and charge fees\n4. Back\n4. Quit\n')

    def showAccMenu(self):
        return input('\n1. Manage account\n2. Open new account\n3. User report\n4. Back\n5. Quit\n')

    def getAccNum(self):
        return input('Enter account number: ')

    def showManAccMenu(self):
        return input('\n1. Deposit\n2. Withdraw\n3. Balance\n4. Charge fee\n5. Close account \n6. Back\n7. Quit\n')

    def showAccounts(self, target_uid, accounts):
        output = '\nAccounts for uid: {0} - '.format(target_uid)
        for account in accounts:
            if account['uid'] == target_uid:
                output += account['acc_num'] + ' '
        print(output + '\n')

    def getAccType(self):
        return input('\n1. Chequing\n2. Saving\n3. Quit\n')

    def getAccName(self):
        return input('Enter account name: ')

    def getDeposit(self):
        return input('Enter deposit amount: ')

    def depositSuccess(self, amount):
        print('\nSuccessfully deposited: ${0}'.format(float(amount)))

    def getWithdraw(self):
        return input('Enter withdraw amount: ')

    def withdrawSuccess(self, amount):
        print('\nSuccessfully withdrew: ${0}'.format(float(amount)))

    def withdrawFailure(self, message):
        print('\nWithdraw failure: {0}'.format(message))

    def getUid(self):
        return input('Enter the user ID: ')

    def showBalance(self, balance):
        print('The current balance is: ', balance)

    def getPIN(self):
        return input('Enter your PIN: ')

    def confirmPIN(self):
        return input('Confirm PIN: ')

    def success(self):
        print('\nSuccessfully logged in.')

    def incorrect(self):
        print('\nIncorrect username password combination')

    def printReport(self, report_content):
        print('\n{0:^65}'.format('----- Beginning of Report -----\n'))
        for item in report_content:
            print(item[0] + '\n')
            for x in range(1, len(item)):
                print(item[x])
            print()
        print('{0:^65}'.format('----- End of Report -----'))

    def int_fee_complete(self):
        print('Successfully completed transactions')

    def close_account_success(self):
        print('Successfully closed account')

    def close_account_fail(self):
        print('Failed to close account. Account balance must be 0')