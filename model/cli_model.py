# cli_db.py
#
# ATM MVC program
#
# Team alroda
#
# Aldrich Huang A01026502 2B
# Robert Janzen A01029341 2B
# David Xiao A00725026 2B

import csv

class CLIModel:
    _ACC_MODEL_FIELDS = ['name', 'pwd']
    
    def __init__(self, file_path):
        self._acc_model_content = []
        self._model_file = file_path
        self.loadAccount()

    def verifyAccount(self, usr, pwd):
        """
            Checks to see that the login credentials are valid
            
        Args:
            usr:
                Username of the account
            pwd:
                Password of the account

        Returns:
            Boolean indicating whether the inputted credentials are valid or not.
        """
        for entry in self._acc_model_content:
            if usr == entry[self._ACC_MODEL_FIELDS[0]]:
                
                if self.verifyPassword(entry[self._ACC_MODEL_FIELDS[1]], pwd):
                    
                    return True
                else:
                    return False
        return False

    def verifyPassword(self, hpwd, pwd):
        """
            Compares the inputted password and the saved password hash, return True if they are the same, false
            otherwise
        Args:
            hpwd:
                password hash
            pwd:
                input password
        Returns:
            Boolean
        """
        
        if self.hashPassword(pwd) == hpwd:
            return True
        else:
            return False
        
    def createAccount(self, usr, pwd):
        """
            Creates a new entry in the account file, which contains the username, and the password hash
            
        Args:
            usr:
                Username for the new account
            pwd:
                Password for the new account
                
        Returns:
            Empty string if successful, error message if failed
        """
        duplicate = False
        message = ''
        for entry in self._acc_model_content:
            if entry[self._ACC_MODEL_FIELDS[0]] == usr:
                message = "User already exists"
                duplicate = True
                break
                
        if not duplicate:
            self._acc_model_content.append({self._ACC_MODEL_FIELDS[0]: usr, self._ACC_MODEL_FIELDS[1]: self.hashPassword(pwd)})
            self.saveAccount()
            
        return message
    
    def loadAccount(self):
        """
            Loads the content of th user account file
            
        Returns:
            None
        """
        try:
            with open(self._model_file) as csv_file:
                reader = csv.DictReader(csv_file)
            
                for row in reader:
                    new_dict = {}
                    for category in self._ACC_MODEL_FIELDS:
                        new_dict[category] = row[category]
                
                    self._acc_model_content.append(new_dict)
        except:
            return
    
    def saveAccount(self):
        """
            Saves value of self._acc_model_content into the user account file
            
        Returns:
            Success message if saved properly, empty string if not saved properly
        """
        message = ''
        try:
            with open(self._model_file, 'w', newline='') as csv_file:
                fields = self._ACC_MODEL_FIELDS
                writer = csv.DictWriter(csv_file, fieldnames=fields)
            
                writer.writeheader()
                for entry in self._acc_model_content:
                    writer.writerow(entry)
                message = "Saved to %s" % self._model_file
        except:
            message = ''
            
        return message
        
    def hashPassword(self, pwd):
        """
            Takes the inputted password and returns the hash
            
        Args:
            pwd:
                Password String
                
        Returns:
            Password hash
        """
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
    pass
