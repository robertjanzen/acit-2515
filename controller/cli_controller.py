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

    def run(self):
        """
            This is the functioned called to start the commandline interface.
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
        """Manage user or create new user"""
        
        uInput = self.view.showUidMenu()
        if uInput == '1':
            self.cli_uid_menu()
        elif uInput == '2':
            self.cli_new_uid()
        elif uInput == '3':
            # self.charge_fees()
            pass
        elif uInput == '4':
            self.run()
        elif uInput == '5':
            exit(0)

    def cli_uid_menu(self):

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

    def cli_choose_account(self, accs):

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
            if msg == 'Chequing' or msg == 'Saving':
                self.view.withdrawSuccess(amount)
                self.trans.create_new_entry(self.uid, msg, self.accNum, 'Deposit', amount)
            else:
                self.view.withdrawFailure(msg)
            self.cli_man_acc()
        elif maInput == '3':
            balance = self.accounts.get_balance(self.uid, self.accNum)
            self.view.showBalance(balance)
            self.cli_man_acc()
        elif maInput == '4':
            # TODO Charge fee
            self.cli_acc_menu()
        elif maInput == '5':
            if self.accounts.delete_account(self.uid, self.accNum):
                self.view.close_account_success()
                self.cli_man_acc()
            else:
                self.view.close_account_fail()
                self.cli_man_acc()
        elif maInput == '6':
            self.cli_acc_menu()
        elif maInput == '7':
            exit(0)


    def cli_create_acc(self):
        tInput = self.view.getAccType()
        if tInput == '1':
            accType = 'Chequing'
        elif tInput == '2':
            accType = 'Savings'
        elif tInput == '3':
            self.cli_acc_menu()
        elif tInput == '4':
            exit(0)
        accName = self.view.getAccName()
        initDep = self.view.getDeposit()
        self.accounts.create_new_account(accType, accName, initDep, self.uid)

    def cli_new_uid(self):
        tInput = self.view.getAccType()
        if tInput == '1':
            accType = 'Chequing'
        elif tInput == '2':
            accType = 'Savings'
        elif tInput == '3':
            exit(0)
        accName = self.view.getAccName()
        initDep = self.view.getDeposit()
        self.uid = self.accounts.create_new_account(accType, accName, initDep)
        self.create_user_db()
        self.accounts.load_accounts()
        self.uidMenu()

    def create_user_db(self):
        cardNum = self.generate_cardNum(self.uid)
        pwdHash = self.hash_password()
        self.userdb.create_new_entry(self.uid, cardNum, pwdHash)

    def generate_cardNum(self, uid):
        init_cardNum = 10000000
        cardNum = init_cardNum+int(uid)
        return str(cardNum)

    def get_password(self):
        inputPwd = self.view.getPIN()
        inputPwd2 = self.view.confirmPIN()
        if inputPwd == inputPwd2:
            return inputPwd

    def hash_password(self):
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