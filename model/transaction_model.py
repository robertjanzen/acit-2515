import datetime
import os
import locale

class TransactionModel:
    _TRANSACTION_COLUMNS = 'date,uid,account_type,account_number,transaction_type,amount'

    def __init__(self):
        pass

    def open_transaction_file(self):
        pass

    def create_new_entry(self, uid, account_type, account_num, transaction_type, amount, date=datetime.datetime.now()):
        row = '{0},{1},{2},{3},{4},{5}'.format(str(date), uid, account_type, account_num, transaction_type, str(float(amount)), )
        self.save_transaction(uid, row)

    # To be used with CLI only
    def delete_from_file(self, uid):
        pass

    # To be used with CLI only
    def edit_entry(self, uid, type, amount):
        pass

    def save_transaction(self, uid, row):
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
                
    def display_report(self, uid):
        filename = 'model/logs/' + str(uid) + '-transactions.csv'
        # filename = 'logs/' + str(uid) + '-transactions.csv'
        report_content = [['Comprehensive report for user no. ' + uid]]
        
        try:
            if os.path.getsize(filename) > 0:
                with open(filename, 'r') as csv_file:
                    transaction_dic = {}
                    log_structure = csv_file.readline()
                    full_file = csv_file.readlines()
                    
                    for line in full_file:
                        line_data = line.rstrip('\n').split(',')
                        account_list = list(transaction_dic.keys())
                        
                        if line_data[3] in account_list:
                            transaction_dic[line_data[3]].append(', '.join(line_data))
                        else:
                            transaction_dic[line_data[3]] = [', '.join(line_data)]
                            
                    account_list.sort(key=float)
                    
                    for account_num in account_list:
                        
                        acc_specific_entry = [('Transactions for account no.' + account_num + '----------')]
                        for entry in transaction_dic[account_num]:
                            acc_specific_entry.append(entry)
                        report_content.append(acc_specific_entry)

            print()
            print('Beginning of Report--------------------------')
            for item in report_content:
                print(item[0])
                print()
                for x in range(1, len(item)):
                    print(item[x])
                print()
            print('End of Report--------------------------------')
            
        except:
            print('Error Generating Report...')
                    
                    


if __name__ == '__main__':
    test = TransactionModel()
    
    test.display_report('1')
