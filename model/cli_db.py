import csv

class CLIDB:
    _ACC_DB_FIELDS = ['name', 'pwd']

    _SP_CHAR_POOL = ['!', '@', '#', '$', '%', '^', '&', '*']
    
    def __init__(self, file_path):
        self._acc_db_content = []
        self._db_file = file_path
        self.loadAcc()
        

    def verifyCLIName(self, name):
        return True

    def verifyPwd(self, pwd):
        return True
    
    def createAcc(self, usr, pwd):
        duplicate = False
        
        for entry in self._acc_db_content:
            if entry[self._ACC_DB_FIELDS[0]] == usr:
                print("User already exists")
                duplicate = True
                break
                
        if not duplicate:
            self._acc_db_content.append({self._ACC_DB_FIELDS[0]: usr, self._ACC_DB_FIELDS[1]: pwd})
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
            
        print(output)
        
    def rvrs_hash(self, hash):
        ascitt_list = []
        output = ''
        
        for character in hash:
            chr_ascii = ord(character)
            
            chr_ascii -= 50
            
            if chr_ascii < ord('!'):
                chr_ascii = chr_ascii - ord('!') + ord('~')
            
            ascitt_list.append(chr_ascii)
        
        for entry in ascitt_list:
            output += chr(entry)
            
        print(output)
        

if __name__ == "__main__":
    test_db = CLIDB('cli_acc_db.csv')
    test_db.createAcc('manager', 'password')
    test_db.pwd_hash('password')
    test_db.rvrs_hash('E6HHLDG9')
    
    
