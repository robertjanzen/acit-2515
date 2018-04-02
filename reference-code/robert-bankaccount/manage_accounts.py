# manage_accounts.py
#
# Bank account program
#
# Robert Janzen A01029341 2B

from chequing import Chequing
from savings import Savings
from term_savings import TermSavings

def main():
    chq = Chequing('Sally', 1000.0)
    sav = Savings('Joe', 5000.0)
    trm = TermSavings('Sally')
    trm.deposit(7000.0)
    sav.deposit(100.0)
    print(sav.balance)
    chq.withdraw(50.0)
    trm.withdraw(50.0)
    print(chq.balance)
    print(trm.balance)
    chq.withdraw(900.0)
    chq.withdraw(100.0)
    trm.charge_min_balance_fee()
    sav.charge_min_balance_fee()
    chq.bounce_fee()
    chq.charge_overdraft_interest()
    sav.pay_interest()
    trm.pay_interest()
    sav.change_name('Joseph')
    print(chq)
    print(sav)
    print(trm)
    chq.transaction_log.list_from_file()
    sav.transaction_log.list_from_file()
    trm.transaction_log.list_from_file()
    trm.term_deposits.list_deposits()

if __name__ == '__main__':
    print('manage_accounts.py...')
    main()