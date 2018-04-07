import csv


class UserDB:
    _DB_COLUMNS = ['uid', 'CardNum', 'hash'];
    def __init__(self, db_file):
        self._db_file = db_file
        self._db_content = []
        
    def open_db_file(self):
        with open(self._db_file, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                new_dict = {}
                for category in self._DB_COLUMNS:
                    new_dict[category] = row[category]
                    
            self._db_content.push(new_dict)
        print(self._db_content)
        