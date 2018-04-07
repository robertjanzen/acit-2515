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

    def showMenu(self):
        return input('\n1. Manage account\n2. Open new account\n3. Quit program\nOption: ')