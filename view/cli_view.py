# cli_view.py
#
# ATM MVC program
#
# Team alroda
#
# Aldrich Huang A01026502 2B
# Robert Janzen A01029341 2B
# David Xiao A00725026 2B

# This presents the CLI view for bank employees
# import getpass

class CLIView:

    def __init__(self):
        # self.getp = getpass.getpass
        pass

    def getCLIName(self):
        """
            Displays a prompt for the user's username
            
        Returns:
            Username inputted by user
        """
        
        user_name = input('Enter your username: ')
        return user_name

    def getCLIPwd(self):
        """
            Displays a prompt for the user's password
            
        Returns:
            Password inputted by user
        """
        
        # password = getp('Enter your password: ')
        password = input('Enter your password: ')
        return password

    def showUidMenu(self):
        """
            Displays a list of available customer management options for the users, then prompts for an input
            
        Returns:
            String containing the user's input, which indicates which option the user selects
        """
        
        print('\nMain menu: ')
        return input('\n1. Manage existing customer\n2. Create new customer\n3. Pay interest and charge fees\n4. Back\n4. Quit\n')

    def showAccMenu(self):
        """
            Display a list of available customer account management options, then prompts the user for an input
            
        Returns:
            String containing the user's input, which indicates which option the user selects
        """
        
        return input('\n1. Manage account\n2. Open new account\n3. User report\n4. Back\n5. Quit\n')

    def getAccNum(self):
        """
            Displays prompt for a valid account number
            
        Returns:
            Account number inputted by the user
        """
        
        return input('Enter account number: ')

    def incorrectAcc(self):
        print('\nSelected account does not exist\n')

    def showManAccMenu(self):
        """
            Displays a list of available management options for the selected account
            
        Returns:
            String containing the user's input, which indicates which option the user selects
        """
        
        return input('\n1. Deposit\n2. Withdraw\n3. Balance\n4. Charge fee\n5. Close account \n6. Back\n7. Quit\n')


    def showAccounts(self, uid, accounts):
        """
            Displays a string which contains a list of account numbers for the accounts that belongs to a uid
            
        Args:
            uid:
                UID tied to a customer
                
            accounts:
                List of account objects
                
        Returns:
            None
        """
        
        # output = '\nAccounts for uid: {0} - '.format(target_uid)
        # for account in accounts:
        #     if account['uid'] == target_uid:
        #         output += account['acc_num'] + ' '
        # print(output + '\n')
        print('\nAccounts for uid: {0} - {1}\n'.format(uid, ' '.join(accounts)))


    def getAccType(self):
        """
            Prompts the user to select an account type
            
        Returns:
            String containing the user input
        """
        
        return input('\n1. Chequing\n2. Saving\n3. Quit\n')

    def getAccName(self):
        """
            Prompts the user to input a new account name
            
        Returns:
            String containing the new account name as inputted by the user
        """
        
        return input('Enter account name: ')

    def getDeposit(self):
        """
            Prompts the user for a value to be deposited to an account
            
        Returns:
            String containing the amount to be deposited
        """
        
        return input('Enter deposit amount: ')
    
    def depositSuccess(self, amount):
        """
            Displays a success message for successful deposit attempts
            
        Args:
            amount:
                Amount that was deposited to an accound

        Returns:
            None
        """
        
        print('\nSuccessfully deposited: ${0}'.format(float(amount)))

    def getWithdraw(self):
        """
            Prompts the user for a value to be withdrawn from an account
            
        Returns:
            String containing the amount to be withdrawn
        """
        
        return input('Enter withdraw amount: ')

    def withdrawSuccess(self, amount):
        """
            Displays a success message for successful withdraw attempts
            
        Args:
            amount:
                Amount that was withdrawn from an account

        Returns:
            None
        """
        
        print('\nSuccessfully withdrew: ${0}'.format(float(amount)))

    def withdrawFailure(self, message):
        """
            Displays a failure message for failed withdraw attempts
            
        Args:
            message:
                String which contains the error message regarding the failed withdraw attempt

        Returns:
            None
        """
        
        print('\nWithdraw failure: {0}'.format(message))

    def getUid(self):
        """
            Promts the user of a UID of a customer
            
        Returns:
            Returns the inputted UID
        """
        
        return input('Enter the user ID: ')

    def showBalance(self, balance):
        """
            Displays the current balance of the selected account
            
        Args:
            balance:
                The current balance of the account
                
        Returns:
            None
        """
        
        print('The current balance is: ', balance)

    def getPIN(self):
        """
            Prompts the user for a new PIN for the customer
            
        Returns:
            The inputted PIN
        """
        
        return input('Enter your PIN: ')

    def confirmPIN(self):
        """
            Displays a confirm prompt which asks the user to re enter the PIN
            
        Returns:
            The inputted PIN
        """
        
        return input('Confirm PIN: ')

    def success(self):
        """
            Displays a success message for successful login attempts
            
        Returns:
            None
        """
        
        print('\nSuccessfully logged in.')

    def incorrect(self):
        """
            Displays a failure message for failed login attempts
            
        Returns:
            None
        """
        
        print('\nIncorrect username password combination\n')

    def printReport(self, report_content):
        """
            Displays a detailed transaction report for the user
            
        Args:
            report_content:
                List of strings containing the transaction log

        Returns:
            None
        """
        
        print('\n{0:^65}'.format('----- Beginning of Report -----\n'))
        for item in report_content:
            print(item[0] + '\n')
            for x in range(1, len(item)):
                print(item[x])
            print()
        print('{0:^65}'.format('----- End of Report -----'))

    def int_fee_complete(self):
        """
            Displays a success message for successful transaction attempts
            
        Returns:
            None
        """
        
        print('Successfully completed transactions')

    def close_account_success(self):
        """
            Displays success message for successful account closure
        Returns:
            None
        """
        
        print('Successfully closed account')

    def close_account_fail(self):
        """
            Displays failure message for failed account closures, this occurs when account has a balance other than 0
        Returns:
            None
        """
        
        print('Failed to close account. Account balance must be 0')