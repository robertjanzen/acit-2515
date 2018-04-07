import csv


class UserDB:
    _DB_COLUMNS = ['uid', 'card_number', 'PIN']
    
    def __init__(self, db_file):
        self._db_file = db_file
        self._db_content = []
        
        self.open_db_file()
        
    @property
    def db_content(self):
        return self._db_content
        
    def open_db_file(self):
        with open(self._db_file) as csv_file:
            reader = csv.DictReader(csv_file)
            
            for row in reader:
                new_dict = {}
                for category in self._DB_COLUMNS:
                    new_dict[category] = row[category]
                    
                self._db_content.append(new_dict)
        
