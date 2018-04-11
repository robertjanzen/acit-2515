# cli_controller.py
#
# ATM MVC program
#
# Team alroda
#
# Aldrich Huang A01026502 2B
# Robert Janzen A01029341 2B
# David Xiao A00725026 2B

from model.account_model import AccountModel
from view.cli_view import CLIView
from model.cli_model import CLIModel
from model.user_model import UserModel
from model.transaction_model import TransactionModel
import random

class CLIController:

    def __init__(self):
        """
            initialize the
            loads imported functions into self parameters
        """
        self.view = CLIView()
        self.cli_model = CLIModel('model/cli_account_model.csv')
        self.accounts = AccountModel()
        self.user_model = UserModel('model/user_model.csv')
        self.transaction_model = TransactionModel()
        self.state = 0
        self.uid = ''
        self.account_number = ''
        self.account_type = ''

    def run(self):
        """
            This is the method called to start the commandline interface.
            Prompts for manager user name and password.
            Calls the uid menu which allows to manager to perform uid tasks.
        """
        choice = False
        while choice == False:
            user_name = self.view.getCLIName()
            password = self.view.getCLIPwd()
            if self.cli_model.verifyAccount(user_name, password):
                choice = True
                self.view.success()
                self.mainMenu()
            else:
                self.view.incorrect()

    def mainMenu(self):
        """
            Called by the run method
            Manage user or create new user

            1. Brings up menu for an existing user
            2. Create new use with a new uid
            3. Charge fees for everyone in database
            4. Back to the previous menu
            5. Exit the command line interface
        """
        
        user_input = self.view.showMainMenu()
        if user_input == '1':
            self.chooseUser()
        elif user_input == '2':
            self.createUser()
        elif user_input == '3':
            self.run()
        elif user_input == '4':
            exit(0)
        else:
            self.mainMenu()

    def chooseUser(self):
        """
            This function first loads existing uid from file and puts it into a list
            If uid exist, go to next menu.
            Else calls view to display error, return this menu and ask for uid.
        """
        uid_list = []
        self.user_model.openModelFile()
        for user in self.user_model.model_content:
            uid_list.append(user['uid'])
        
        if not uid_list:
            self.view.noUID()
            self.mainMenu()
        else:
            choice = False
            while choice == False:
                self.uid = self.view.getUid()
                if self.uid in uid_list:
                    choice = True
                    self.manageUser()
                else:
                    break
                    
            self.view.incorrectUID()
            self.chooseUser()

    def manageUser(self):
        """
            Create a list of account associated with this uid
            Presents the options to manage this uid

            1. Manage an existing account from the list
                check to see if there are any accounts, if not then need to create account
                if there are accounts then pass into the chooseAccount method a list
            2. Create a new account for this uid
            3. Print out the transaction report for this uid
            4. Back to the UID selection menu
            5. Quit program
        :return:
        """
        self.accounts.loadAccount()
        self.state = 1
        user_input = self.view.showAccMenu()
        if user_input == '1':

            account_list = []
            for index, account in enumerate(self.accounts.accounts):
                if account['uid'] == self.uid:
                    account_list.append(self.accounts.accounts[index]['acc_num'])

            if not account_list:
                self.view.noAccounts()
                self.manageUser()
            else:
                self.chooseAccount(account_list)
        elif user_input == '2':
            self.createAccount()
            self.manageUser()
        elif user_input == '3':
            self.getReport()
            self.manageUser()
        elif user_input == '4':
            self.mainMenu()
        elif user_input == '5':
            exit(0)
        else:
            self.manageUser()

    def chooseAccount(self, accs):
        """
            Takes a input account number from commandline, checks if the number entered is in list.
        :param accs:list of accounts for this uid
        """
        self.view.showAccounts(self.uid, accs)
        choice = False
        while choice == False:
            self.account_number = self.view.getAccNum()
            if self.account_number in accs:
                choice = True
            else:
                self.view.incorrectAcc()
        self.manageAccount()

    def manageAccount(self):
        """
            Menu to manage an existing account.
            1. Prompt user for a deposit amount, update and write to file
            2. Prompt user for a withdraw amount, update and write to file
            3. Returns account balance for this account
            4. Delete this account, only works if account balance = 0
            5. Back to previous menu
            6. Exit program
        """
        self.accounts.loadAccount()
        user_input = self.view.showManAccMenu()
        if user_input == '1':
            amount = self.view.getDeposit()
            acc_type = self.accounts.deposit(self.uid, self.account_number, amount)
            self.transaction_model.createNewEntry(self.uid, acc_type, self.account_number, 'Deposit', amount)
            self.view.depositSuccess(str(round(float(amount), 2)))
            self.manageAccount()
        elif user_input == '2':
            amount = self.view.getWithdraw()
            msg = self.accounts.withdraw(self.uid, self.account_number, amount)
            if msg == '':
                account_type = self.accounts.getAccountType(self.uid, self.account_number)
                self.view.withdrawSuccess(str(round(float(amount), 2)))
                if account_type != '':
                    self.transaction_model.createNewEntry(self.uid, account_type, self.account_number, 'Withdraw', amount)
                else:
                    pass
            else:
                self.view.withdrawFailure(msg)
            self.manageAccount()
        elif user_input == '3':
            balance = self.accounts.getBalance(self.uid, self.account_number)
            self.view.showBalance(balance)
            self.manageAccount()
        elif user_input == '4':
            selected_acc_type = self.accounts.getAccountType(self.uid, self.account_number)
            if self.accounts.deleteAccount(self.uid, self.account_number):
                new_msg = 'Account closed'
                self.transaction_model.createNewActionEntry(self.uid, selected_acc_type, self.account_number, new_msg)
                self.view.close_account_success()
                self.mainMenu()
            else:
                self.view.close_account_fail()
                self.manageAccount()
        elif user_input == '5':
            self.manageUser()
        elif user_input == '6':
            exit(0)
        else:
            self.manageAccount()

    def createAccount(self):
        """
            Method to create a new account for an existing user.
            Previous function sets the uid to use.
            This function gets the desired account name from user
            Gets the initial deposit amount from user
            Use the account_model to create new accout and write to file
        """
        user_input = self.view.getAccType()
        if user_input == '1':
            account_type = 'Chequing'
        elif user_input == '2':
            account_type = 'Savings'
        elif user_input == '3':
            self.manageUser()
        elif user_input == '4':
            self.manageAccount()
        else:
            self.createAccount()
        account_name = self.view.getAccName()
        deposit_amount = self.view.getDeposit()
        new_acc_num = self.accounts.createNewAccount(account_type, account_name, deposit_amount, self.uid)
        new_msg = 'Account created with balance of: ${}'.format(str(round(float(deposit_amount), 2)))
        self.transaction_model.createNewActionEntry(self.uid, account_type, new_acc_num, new_msg)
        self.view.accountCreationSuccess(new_acc_num)

    def createUser(self):
        """
            Method to create a new user, requires creating an account associated with the uid
            1. Chequing account
            2. Saving account
            3. Go back
            returns to uid menu once account is created successfully
        """
        user_input = self.view.getAccType()
        if user_input == '1':
            account_type = 'Chequing'
        elif user_input == '2':
            account_type = 'Savings'
        elif user_input == '3':
            self.mainMenu()
        else:
            self.createUser()
        account_name = self.view.getAccName()
        deposit_amount = self.view.getDeposit()
        self.accounts.createNewAccount(account_type, account_name, deposit_amount)
        self.uid = self.accounts.accounts[-1]['uid']
        self.account_number = self.accounts.accounts[-1]['acc_num']
        new_msg = 'Account created with balance of: ${}'.format(str(round(float(deposit_amount), 2)))
        self.transaction_model.createNewActionEntry(self.uid, account_type, self.account_number, new_msg)
        self.generateUser()
        self.view.userCreationSuccess(self.uid)
        self.accounts.loadAccount()
        self.mainMenu()

    def generateUser(self):
        """
            Method to create a new user
            Generate a card number
            Generate a hashed PIN
            Calls user_model method to create new user and write to file
        """
        card_number = self.generateCardNum(self.uid)
        hashed_password = self.hashPassword()
        self.user_model.createNewEntry(self.uid, card_number, hashed_password)

    def generateCardNum(self, uid):
        """
            This function creates a card_number starting from 10000000 and uid.
        :param uid:uid of this user
        :return: card_number string
        """
        init_cardNum = 10000000
        card_number = init_cardNum+int(uid)
        return str(card_number)

    def getPassword(self):
        """
            Prompts user to enter and re-enter PIN.
            Check is PIN match and returns it to hashPassword
        :return: inputPwd
        """
        valid_PIN = False
        while not valid_PIN:
            inputPwd = self.view.getPIN()
            inputPwd2 = self.view.confirmPIN()
            
            if inputPwd == inputPwd2:
                try:
                    int(inputPwd)
                    valid_PIN = True
                except:
                    self.view.non_numeric_PIN()
                    valid_PIN = False
            else:
                self.view.PIN_mismatch()
            
        return inputPwd

    def hashPassword(self):
        """
            Creates a hashed password based on the commandline input
             and returns it to the generateUser method
        :return: hash_str
        """
        pwd = self.getPassword()
        hash_str = str(int(pwd[0])*2)
        odd_num = ['3', '5', '7', '9']
        for strIndex in range(1,len(pwd)):
            odd_str = ''
            for rand_num in range(random.randint(1,6)):
                odd_str += random.choice(odd_num)
            hash_str +=(odd_str+str(int(pwd[strIndex])*2))
        return hash_str

    def getReport(self):
        report = self.transaction_model.displayReport(self.uid)
        self.view.printReport(report)


if __name__ == "__main__":
    controller = CLIController()
    controller.run()