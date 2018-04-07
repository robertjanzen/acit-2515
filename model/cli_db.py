import csv

class CLIDB:
    _ACC_DB_FIELDS = ['name', 'pwd']
    
    def __init__(self, file_path):
        self._acc_db_content = []
        self._db_file = file_path
        self.loadAcc()
        

    def verify_account(self, usr, pwd):
        for entry in self._acc_db_content:
            if usr == entry[self._ACC_DB_FIELDS[0]]:
                if self.verifyPwd(entry[self._ACC_DB_FIELDS[1]], pwd):
                    return True
                else:
                    return False
        return False

    def verifyPwd(self, hpwd, pwd):
        if self.pwd_hash(pwd) == hpwd:
            return True
        else:
            return False
        
    def createAcc(self, usr, pwd):
        duplicate = False
        
        for entry in self._acc_db_content:
            if entry[self._ACC_DB_FIELDS[0]] == usr:
                print("User already exists")
                duplicate = True
                break
                
        if not duplicate:
            self._acc_db_content.append({self._ACC_DB_FIELDS[0]: usr, self._ACC_DB_FIELDS[1]: self.pwd_hash(pwd)})
            self.saveAcc()
    
    def loadAcc(self):
        try:
            with open(self._db_file) as csv_file:
                reader = csv.DictReader(csv_file)
            
                for row in reader:
                    new_dict = {}
                    for category in self._ACC_DB_FIELDS:
                        new_dict[category] = row[category]
                
                    self._acc_db_content.append(new_dict)
        except:
            return
    
    def saveAcc(self):
        
        try:
            with open(self._db_file, 'w', newline='') as csv_file:
                fields = self._ACC_DB_FIELDS
                writer = csv.DictWriter(csv_file, fieldnames=fields)
            
                writer.writeheader()
                for entry in self._acc_db_content:
                    writer.writerow(entry)
                print("Saved to %s" % self._db_file)
        except:
            return
        
    def pwd_hash(self, pwd):
        ascii_list = []
        output = ''
        for character in pwd:
            chr_ascii = ord(character)
            
            chr_ascii += 50
            if chr_ascii > ord('~'):
                chr_ascii = chr_ascii - ord('~') + ord('!')
            
            ascii_list.append(chr_ascii)
            
        for entry in ascii_list:
            output += chr(entry)
            
        return output


if __name__ == "__main__":
    test_db = CLIDB('cli_acc_db.csv')
    test_db.createAcc('manager', 'password')
    print(test_db.verify_account('manager', 'password'))
