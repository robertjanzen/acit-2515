# button_controller.py
#
# ATM MVC program
#
# Team alroda
#
# Aldrich Huang A01026502 2B
# Robert Janzen A01029341 2B
# David Xiao A00725026 2B

import csv

class UserModel:
    _MODEL_COLUMNS = ['uid', 'card_number', 'PIN']
    
    def __init__(self, model_file):
        self._model_file = model_file
        self._model_content = []
        
        self.openModelFile()
        
    @property
    def model_content(self):
        """
            Getter for the instance variable: self._model_content
            
        Returns:
            Value of self._model_content
        """
        return self._model_content
        
    def openModelFile(self):
        """
            Opens the data file and saves the content to the instance variable: self._model_content
            
        Returns:
            None
        """
        with open(self._model_file) as csv_file:
            reader = csv.DictReader(csv_file)
            self._model_content = []
            for row in reader:
                new_dict = {}
                for category in self._MODEL_COLUMNS:
                    new_dict[category] = row[category]
                    
                self._model_content.append(new_dict)

    def createNewEntry(self, input_uid, input_cardnum, input_hash):
        """
            Takes inputted data then checks for duplicate card number in existing user account entries. Creates a new
            entry and saves to file of no duplicate is found.
            
        Args:
            input_uid:
                User ID of the user
            input_cardnum:
                Card number of the user's bank card
            input_hash:
                Hashed PIN tied to the card number

        Returns:
            None
        """
        new_entry = {self._MODEL_COLUMNS[0]: input_uid,
                     self._MODEL_COLUMNS[1]: input_cardnum,
                     self._MODEL_COLUMNS[2]: input_hash}
        
        duplicate = False
        
        for entry in self.model_content:
            if entry['uid'] == new_entry['uid']:
                duplicate = True
                
        if not duplicate:
            self._model_content.append(new_entry)
            self.saveToFile()

    def deleteFromFile(self, input_uid):
        """
            Deletes an entry from the user database
            
        Args:
            input_uid:
                The UID of the user whose account is to be deleted

        Returns:
            None
        """
        for x in range(len(self.model_content)):
            if self.model_content[x]['uid'] == input_uid:
                del self._model_content[x]
                self.saveToFile()
                break
                
    def editEntry(self, input_uid, input_category, input_value):
        """
            Edits the user account. Does not allow uid to be edited
            
        Args:
            input_uid:
                UID tied of the accound
            input_category:
                The field of the entry to be edited
            input_value:
                The new value for the data field

        Returns:
            None
        """
        for item in self.model_content:
            if item['uid'] == input_uid:
                if input_category in self._MODEL_COLUMNS and not 'uid':
                    item[input_category] = input_value
                    self.saveToFile()
                    break
    
    def saveToFile(self):
        """
            Saves the value of the instance variable: self._model_content to the csv file
            
        Returns:
            None
        """
        with open(self._model_file, 'w', newline='') as csv_file:
            fields = self._MODEL_COLUMNS
            writer = csv.DictWriter(csv_file, fieldnames=fields)
        
            writer.writeheader()
            for entry in self.model_content:
                writer.writerow(entry)

if __name__ == "__main__":
    test = UserModel('model/user_model.csv')
    test.createNewEntry('10000', '3333333333', '232323232')
