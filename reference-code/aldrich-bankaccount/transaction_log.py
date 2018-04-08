from log_entry import Entry
from constants import *


class TransactionLog:
    def __init__(self, acc_num):
        """
            Constructor for creating an instance of the class TransactionLog. The instance contains the attribute
            contains a list of Entry objects, which are the recorded transactions of the related account.
            Creates/overwrites a log file to save the transaction log to.
            
        Args:
            acc_num:    Accounted number of the account the TransactionLog belongs to
        """
        
        self.acc_num = acc_num
        self.output_file = LOG_FILE_NAME_FORMAT.format(self.acc_num)
        self.session_log = []
        
        self.create_log_file()
        
    def update_log(self, tx_type, tx_param=""):
        """
            Opens the log file for appending, then appends a new entry to the log file.
            
        Args:
            tx_type:    Type of transaction to be recorded
            tx_param:   Parameters of the transaction to be recorded

        Returns:
            Nothing
        """
        
        file = open(self.output_file, 'a+')

        new_entry = Entry(self.acc_num, tx_type, tx_param)
        self.session_log.append(new_entry)
        file.write(new_entry.log)

        file.close()

    def get_log(self):
        """
            Opends the log file and returns the formatted content of the file.
            
        Returns:
            Formatted string containing the content of the log file
        """
        
        output_string = "\n"

        file = open(self.output_file, 'r')

        output_string += '\n'.join([entry.rstrip() for entry in (file.readlines())])
        file.close()
        return output_string

    def get_session_log(self):
        """
            Gets the list of transactions recorded in the current usage session.
        Returns:
            String containing the list of recorded transactions for the current session
        """
        
        output_string = "Current Session:\n"
        for entry in self.session_log:
            output_string += entry.log
        return output_string
    
    def create_log_file(self):
        """
            Creates a new log file or overwrites an existing if one with the same name already exists.
            
        Returns:
            Nothing
        """
        
        file = open(self.output_file, 'w+')
        file.write("")
        file.close()
        
    def clear_session_log(self):
        """
            Clears the recorded session_log
            
        Returns:
            Nothing
        """
        
        self.session_log = []
        
        
def test():
    """
        Function for testing the functionality of the class TransactionLog
    Returns:
        Nothing
    """
    
    new_log = TransactionLog("log_test")
    new_log.update_log("Deposit", "$900")
    new_log.update_log("Deposit", "$900")
    new_log.update_log("Deposit", "$900")
    new_log.update_log("Deposit", "$900")
    new_log.update_log("Deposit", "$901")
    print(new_log.get_log())
    print(new_log.get_session_log())
    new_log.clear_session_log()
    new_log.update_log("Deposit", "$901")
    new_log.update_log("Deposit", "$900")
    print(new_log.get_log())
    print(new_log.get_session_log())


if __name__ == "__main__":
    test()
