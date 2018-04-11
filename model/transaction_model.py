# transaction_model.py
#
# ATM MVC program
#
# Team alroda
#
# Aldrich Huang A01026502 2B
# Robert Janzen A01029341 2B
# David Xiao A00725026 2B

import datetime
import os

class TransactionModel:
    _TRANSACTION_COLUMNS = 'date,uid,account_type,account_number,transaction_type,amount'

    def __init__(self):
        pass

    def createNewEntry(self, uid, account_type, account_num, transaction_type, amount, date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
        """
            Creates a new transaction log entry to be saved to file
            
        Args:
            uid:
                UID of the user that owns the account that the transaction is initiated from
            account_type:
                The type of the account
            account_num:
                The account number of the account
            transaction_type:
                The type of transaction that was done
            amount:
                The dollar value involved in the transaction
            date:
                The time and date when the transaction took place

        Returns:
            None
        """
        row = '{0},{1},{2},{3},{4},{5}'.format(date, uid, account_type, account_num, transaction_type, str(float(amount)), )
        self.saveTransaction(uid, row)

    def saveTransaction(self, uid, row):
        """
            Saves the new entry to the transaction log file
            
        Args:
            uid:
                UID of the user who owns that account that initiated the transaction
            row:
                String containing the new entry to be added to the transaction log file
                
        Returns:
            None
        """
        filename = 'model/logs/'+str(uid)+'-transactions.csv'
        try:
            if os.path.getsize(filename) > 0:
                with open(filename, 'a') as csv_file:
                    csv_file.write('\n'+row)
            else:
                with open(filename, 'w') as csv_file:
                    output = self._TRANSACTION_COLUMNS + '\n' + row
                    csv_file.write(output)
        except OSError:
            with open(filename, 'w') as csv_file:
                output = self._TRANSACTION_COLUMNS + '\n' + row
                csv_file.write(output)
                
    def createNewActionEntry(self, uid, account_type, account_num, action_type, date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
        """
            Creates a new account action entry in the transaction log
        Args:
            uid:
                uid of the user who owns the accound
            account_type:
                type of the account
            account_num:
                account number of the account
            action_type:
                string describing the type of action done to the account
            date:
                current date
        Returns:
            None
        """
        row = '{0},{1},{2},{3},{4}'.format(date, uid, account_type, account_num, action_type)
        self.saveTransaction(uid, row)
                
    def displayReport(self, uid):
        """
            Displays a report of all recorded transactions for accounts owned by the User with the ID uid. The report
            is displayed in the CLI
            
        Args:
            uid:
                UID of the user
                
        Returns:
            None
        """
        filename = 'model/logs/' + str(uid) + '-transactions.csv'
        report_content = [['Comprehensive report for user no. ' + uid]]

        try:
            if os.path.getsize(filename) > 0:
                with open(filename, 'r') as csv_file:
                    transaction_dic = {}
                    
                    csv_file.readline()
                    full_file = csv_file.readlines()

                    account_list = []
                    
                    for line in full_file:
                        
                        line_data = line.rstrip('\n').split(',')
                        
                        if line_data[3] in account_list:
                            transaction_dic[line_data[3]].append(', '.join(line_data))
                        else:
                            transaction_dic[line_data[3]] = [', '.join(line_data)]
                            
                        account_list = list(transaction_dic.keys())
                        
                    account_list.sort(key=str)
                    
                    for account_num in account_list:

                        acc_specific_entry = [('Transactions for account no.' + account_num)]
                        for entry in transaction_dic[account_num]:
                            acc_specific_entry.append(entry)
                        report_content.append(acc_specific_entry)

                return report_content
        except:
            return 'Error Generating Report...'

if __name__ == '__main__':
    test = TransactionModel()
    test.displayReport('1')
