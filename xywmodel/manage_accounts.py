# A00725026 David Xiao
# This is the main test function for this program

from chequing import Chequing
from saving import Saving
from termsaving import TermSaving

def main():
    accSally = Chequing('Sally', 1000)
    accJoe = Saving('Joe', 5000)
    accSally2 = TermSaving('Sally', 7000)
    accJoe.deposit(100)
    print(accSally)
    print(accJoe)
    print(accSally2)
    print()

    accSally.withdraw(50)
    accSally2.withdraw(50)
    print(accSally)
    print(accJoe)
    print(accSally2)
    print()

    accSally.withdraw(200)
    accSally.withdraw(1000)
    print(accSally)
    print(accJoe)
    print(accSally2)
    print()

    accSally.charge_interest()
    accJoe.charge_fee()
    accSally2.charge_fee()
    print(accSally)
    print(accJoe)
    print(accSally2)
    print()

    accJoe.pay_interest()
    accSally2.pay_interest()
    print(accSally)
    print(accJoe)
    print(accSally2)
    print()

    accJoe.change_name('Joseph')
    print(accSally)
    print(accJoe)
    print(accSally2)
    print()

    accSally.show_transaction()
    print()
    accJoe.show_transaction()
    print()
    accSally2.show_transaction()
    print()


if __name__ == '__main__':
    main()