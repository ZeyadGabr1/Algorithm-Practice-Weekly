from cryptography.fernet import Fernet
from file_manger import FileManger

class Encrypt_Decrypt:

    key = FileManger.load_key_data()
    chiper = Fernet(key)

    @classmethod
    def encrypt_text(cls, text : str):

        secure_text = cls.chiper.encrypt(text.encode()).decode()

        return secure_text


    
    @classmethod
    def decrypt_text(cls, text_place):

        text = cls.chiper.decrypt(text_place).decode()
        return text
        




