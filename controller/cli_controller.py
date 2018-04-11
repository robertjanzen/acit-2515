from model.account_model import AccountModel
from view.cli_view import CLIView
from model.cli_db import CLIDB
from model.user_model import UserDB
from model.transaction_model import TransactionModel
import random


class CLIController:

    def __init__(self):
        """
            initialize the
            loads imported functions into self parameters
        """
        self.view = CLIView()
        self.clidb = CLIDB('model/cli_acc_db.csv')
        self.accounts = AccountModel()
        self.userdb = UserDB('model/user_db.csv')
        self.trans = TransactionModel()
        self.state = 0
        self.uid = ''
        self.accNum = ''
        self.accType = ''

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
            if self.clidb.verify_account(user_name, password):
                choice = True
                self.view.success()
                self.uidMenu()
            else:
                self.view.incorrect()

    def uidMenu(self):
        """
            Called by the run method
            Manage user or create new user

            1. Brings up menu for an existing user
            2. Create new use with a new uid
            3. Charge fees for everyone in database
            4. Back to the previous menu
            5. Exit the command line interface
        """
        
        uInput = self.view.showUidMenu()
        if uInput == '1':
            self.cli_uid_menu()
        elif uInput == '2':
            self.cli_new_uid()
        elif uInput == '3':
            self.run()
        elif uInput == '4':
            exit(0)
        else:
            self.uidMenu()

    def cli_uid_menu(self):
        """
            This function first loads existing uid from file and puts it into a list
            If uid exist, go to next menu.
            Else calls view to display error, return this menu and ask for uid.
        """
        uid_list = []
        self.userdb.open_db_file()
        for user in self.userdb.db_content:
            uid_list.append(user['uid'])
        
        if not uid_list:
            self.view.noUID()
            self.uidMenu()
        else:
            choice = False
            while choice == False:
                self.uid = self.view.getUid()
                if self.uid in uid_list:
                    choice = True
                    self.cli_acc_menu()
                else:
                    break
                    
            self.view.incorrectUID()
            self.cli_uid_menu()

    def cli_acc_menu(self):
        """
            Create a list of account associated with this uid
            Presents the options to manage this uid

            1. Manage an existing account from the list
                check to see if there are any accounts, if not then need to create account
                if there are accounts then pass into the cli_choose_account method a list
            2. Create a new account for this uid
            3. Print out the transaction report for this uid
            4. Back to the UID selection menu
            5. Quit program
        :return:
        """
        self.accounts.load_accounts()
        self.state = 1
        aInput = self.view.showAccMenu()
        if aInput == '1':

            account_list = []
            for index, account in enumerate(self.accounts.accounts):
                if account['uid'] == self.uid:
                    account_list.append(self.accounts.accounts[index]['acc_num'])

            if not account_list:
                self.view.noAccounts()
                self.cli_acc_menu()
            else:
                self.cli_choose_account(account_list)
        elif aInput == '2':
            self.cli_create_acc()
            self.cli_acc_menu()
        elif aInput == '3':
            self.get_report()
            self.cli_acc_menu()
        elif aInput == '4':
            self.uidMenu()
        elif aInput == '5':
            exit(0)
        else:
            self.cli_acc_menu()

    def cli_choose_account(self, accs):
        """
            Takes a input account number from commandline, checks if the number entered is in list.
        :param accs:list of accounts for this uid
        """
        self.view.showAccounts(self.uid, accs)
        choice = False
        while choice == False:
            self.accNum = self.view.getAccNum()
            if self.accNum in accs:
                choice = True
            else:
                self.view.incorrectAcc()
        self.cli_man_acc()

    def cli_man_acc(self):
        """
            Menu to manage an existing account.
            1. Prompt user for a deposit amount, update and write to file
            2. Prompt user for a withdraw amount, update and write to file
            3. Returns account balance for this account
            4. Delete this account, only works if account balance = 0
            5. Back to previous menu
            6. Exit program
        """
        self.accounts.load_accounts()
        maInput = self.view.showManAccMenu()
        if maInput == '1':
            amount = self.view.getDeposit()
            acc_type = self.accounts.deposit(self.uid, self.accNum, amount)
            self.trans.create_new_entry(self.uid, acc_type, self.accNum, 'Deposit', amount)
            self.view.depositSuccess(amount)
            self.cli_man_acc()
        elif maInput == '2':
            amount = self.view.getWithdraw()
            msg = self.accounts.withdraw(self.uid, self.accNum, amount)
            if msg == '':
                accType = self.accounts.getAccountType(self.uid, self.accNum)
                self.view.withdrawSuccess(amount)
                if accType != '':
                    self.trans.create_new_entry(self.uid, accType, self.accNum, 'Withdraw', amount)
                else:
                    pass
            else:
                self.view.withdrawFailure(msg)
            self.cli_man_acc()
        elif maInput == '3':
            balance = self.accounts.get_balance(self.uid, self.accNum)
            self.view.showBalance(balance)
            self.cli_man_acc()
        elif maInput == '4':
            if self.accounts.delete_account(self.uid, self.accNum):
                self.view.close_account_success()
                self.uidMenu()
            else:
                self.view.close_account_fail()
                self.cli_man_acc()
        elif maInput == '5':
            self.cli_acc_menu()
        elif maInput == '6':
            exit(0)
        else:
            self.cli_man_acc()


    def cli_create_acc(self):
        """
            Method to create a new account for an existing user.
            Previous function sets the uid to use.
            This function gets the desired account name from user
            Gets the initial deposit amount from user
            Use the account_model to create new accout and write to file
        """
        tInput = self.view.getAccType()
        if tInput == '1':
            accType = 'Chequing'
        elif tInput == '2':
            accType = 'Savings'
        elif tInput == '3':
            self.cli_acc_menu()
        elif tInput == '4':
            self.cli_man_acc()
        else:
            self.cli_create_acc()
        accName = self.view.getAccName()
        initDep = self.view.getDeposit()
        new_acc_num = self.accounts.create_new_account(accType, accName, initDep, self.uid)
        self.view.accountCreationSuccess(new_acc_num)

    def cli_new_uid(self):
        """
            Method to create a new user, requires creating an account associated with the uid
            1. Chequing account
            2. Saving account
            3. Go back
            returns to uid menu once account is created successfully
        """
        tInput = self.view.getAccType()
        if tInput == '1':
            accType = 'Chequing'
        elif tInput == '2':
            accType = 'Savings'
        elif tInput == '3':
            self.cli_new_uid()
        else:
            self.cli_new_uid()
        accName = self.view.getAccName()
        initDep = self.view.getDeposit()
        self.uid = self.accounts.create_new_account(accType, accName, initDep)
        self.create_user_db()
        self.view.userCreationSuccess(self.uid)
        self.accounts.load_accounts()
        self.uidMenu()

    def create_user_db(self):
        """
            Method to create a new user
            Generate a card number
            Generate a hashed PIN
            Calls user_model method to create new user and write to file
        """
        cardNum = self.generate_cardNum(self.uid)
        pwdHash = self.hash_password()
        self.userdb.create_new_entry(self.uid, cardNum, pwdHash)

    def generate_cardNum(self, uid):
        """
            This function creates a cardNum starting from 10000000 and uid.
        :param uid:uid of this user
        :return: cardNum string
        """
        init_cardNum = 10000000
        cardNum = init_cardNum+int(uid)
        return str(cardNum)

    def get_password(self):
        """
            Prompts user to enter and re-enter PIN.
            Check is PIN match and returns it to hash_password
        :return: inputPwd
        """
        inputPwd = self.view.getPIN()
        inputPwd2 = self.view.confirmPIN()
        if inputPwd == inputPwd2:
            return inputPwd

    def hash_password(self):
        """
            Creates a hashed password based on the commandline input
             and returns it to the create_user_db method
        :return: hash_str
        """
        pwd = self.get_password()
        hash_str = str(int(pwd[0])*2)
        odd_num = ['3', '5', '7', '9']
        for strIndex in range(1,len(pwd)):
            odd_str = ''
            for rand_num in range(random.randint(1,6)):
                odd_str += random.choice(odd_num)
            hash_str +=(odd_str+str(int(pwd[strIndex])*2))
        return hash_str

    def get_report(self):
        report = self.trans.display_report(self.uid)
        self.view.printReport(report)

    # def charge_fees(self):
    #     self.accounts.interest_and_fee()
    #     self.view.int_fee_complete()

if __name__ == "__main__":
    controller = CLIController()
    controller.run()