import json
import os
import pandas as pd
from cryptography.fernet import Fernet
class FileManger:
    
    # Database Name
    FILE_DATA_NAME = 'to_do_tasks.json'
    KEY_FILE_NAME = 'key.key'
    path = os.getcwd()

    @classmethod 
    def load_data(cls):
        """Reload Data From The Main File"""
        #code

        try: # try to open the file In Read Mode To Recovry The Data When App Start if file Found Return The All Data
            with open(cls.FILE_DATA_NAME, 'r')as file:
                return json.load(file)
            
        # If File Not Found Return A empty Set
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        
    @classmethod    
    def save_data(cls, data):
        """Save The New Data In The Main File"""
        #code

        with open(cls.FILE_DATA_NAME, 'w')as file:
            json.dump(data, file, indent=5)


    @classmethod
    def load_key_data(cls):
        try:

            with open(cls.KEY_FILE_NAME, 'rb')as file:
                return file.read()
            
        except FileNotFoundError:
            return cls.crete_new_key()
        
    @classmethod
    def save_data_key(cls, key):

        with open(cls.KEY_FILE_NAME, 'wb')as file:
            file.write(key)

    

        
        
    @classmethod
    def crete_new_key(cls):
        key = Fernet.generate_key()
        cls.save_data_key(key)
        return key



    @classmethod
    def check_file_place(cls, file_name):

        if os.path.exists(f"{cls.path}/{file_name}.csv"):
            return True
        
        return False
    
    
    @classmethod
    def create_csv_file(cls, data, file_name):

        if cls.check_file_place(file_name):
            return False
        
        else:

            file = pd.DataFrame(data)

            file.to_csv(f"{cls.path}/{file_name}.csv", index=False)

            return True
        


        






    

