from datetime import datetime
from constants import *


class Entry:
    def __init__(self, acc_num, tx_type, tx_param=""):
        """
            Constructor for creating an instance of the class Entry. The class contains the current date and time and a
            formatted string which is the an entry to the class TransactionLog.
            
        Args:
            acc_num:    Account number of then account the entry is related to
            tx_type:    Type of transaction to be recorded
            tx_param:   Transaction parameter to be recorded
        """
        
        self.date = datetime.now().date()
        self.time = datetime.now().time().strftime(LOG_TIME_FORMAT)
        self.content = LOG_ENTRY_FORMAT.format(self.curr_time, acc_num, tx_type, tx_param)

    @property
    def curr_time(self):
        """
            Returns a formatted string of the current time.
            
        Returns:
            Formatted string depicting the current time
        """
        
        return "{}".format(self.date) + " " + "{: <10}".format(self.time)

    @property
    def log(self):
        """
            Returns the formatted string of the transaction Entry.
            
        Returns:
            Formatted string of the recorded transaction Entry
        """
        return self.content

    def __str__(self):
        """
            Returns transaction log entry.
            
        Returns:
            Transaction log entry
        """
        return self.log


def test():
    """
        Functionality for testing the attributes and methods of the class Entry
    Returns:
        Nothing
    """
    
    test_log = Entry("000001", "Deposit", "$999.99")
    print(test_log)


if __name__ == "__main__":
    test()
