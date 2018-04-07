import datetime
# from translog import Translog


class Transaction():
    def __init__(self, accNum, type, tx_amount):
        """This function creates an instance of a log"""
        self.now = datetime.datetime.now()
        self.accNum = accNum
        self.type = type
        self.tx_amount = tx_amount
        # self.write_log()

    def __str__(self):
        """this method returns the log as a line of string"""
        return '{} {:>7} {:<10} {}'.format(str(self.now.strftime("%Y-%m-%d %H:%M:%S")), str(self.accNum), str(self.type), str(self.tx_amount))

    # def write_log(self):
    #     t.add_entry(self.__str__())

if __name__ == '__main__':
    # t = Translog()
    b = Transaction('10000', 'wd', 10000)
    c = Transaction('10001', 'dp', 50000)
