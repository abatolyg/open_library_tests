# config/config.py
import os
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from dotenv import load_dotenv
from ..utils.pwd_manager import PasswordManager

class Config:

    # Static data members

    #user cridentals to be specified here and taken from 
    WEB_LOGIN_EMAIL = os.getenv("WEB_LOGIN_EMAIL", "anatolyg@gmail.com") 
    API_LOGIN_ACCESS = os.getenv("API_LOGIN_ACCESS", 'UQRbDYVkNyeGa8Vw') 
    API_LOGIN_SECRET = os.getenv("API_LOGIN_SECRET", 'XgqOHGMyS5XMsGba') 
              
    #webdriver config from env variables can be done for each test. if not exists 
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    WAIT_FOR_WEB_ELEMENT_TIMEOUT = os.getenv("WAIT_FOR_WEB_ELEMENT_TIMEOUT", 10)
         
    #web access urls
    BASE_URL = os.getenv("BASE_URL", "https://openlibrary.org") 

    # dynamic 
    WEB_LOGIN_URL = f"{BASE_URL}/account/login"
    API_LOGIN_URL = f"{BASE_URL}/account/login"

    WEB_USER = WEB_LOGIN_EMAIL.split('@')[0]       
          
    @staticmethod
    def get_password_decrypted():
       
         # Load environment variables from .env file
         load_dotenv()

        # Create an instance of PasswordManager
         password_manager = PasswordManager()

        # Get password from environment variable
         password_encripted = os.getenv("WEB_PASSWORD_ENCRYPTED")

         if password_encripted:
            # Decrypt the password
            password_decrypted = password_manager.decrypt_password(password_encripted)
            print(f"Decrypted: {password_decrypted}")
            return password_decrypted    
         else:
            print("Password not found in environment variables.")
            return password_decrypted    




    