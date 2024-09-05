import requests
from ..config.config import Config
from ..utils.logger import setup_logger


# Service Layer Pattern  -  service layer that interacts with the REST API.
# 
class BaseAPI():
    
    ERROR_CODE_SUCESS = 200

    def __init__(self):
        self.session = requests.Session()
        self.logger = setup_logger(__name__)
        # Add any necessary authentication here
        self.session_cookie = None

    def login_to_openlibrary(self):
        ret_val = None
        url = Config.API_LOGIN_URL
        headers = {'Content-Type': 'application/json'}
        data = {
            "access": Config.API_LOGIN_ACCESS,
            "secret": Config.API_LOGIN_SECRET
        }

        response = requests.post(url, headers=headers, json=data)
    
        if response.status_code == BaseAPI.ERROR_CODE_SUCESS:
            self.logger.info(f"Login successful!")
            # Extract the Set-Cookie header
            self.session_cookie = response.headers.get('Set-Cookie')
            ret_val = self.session_cookie
        else:
            self.logger.error(f"Failed to login: {response.status_code}")

        return ret_val 