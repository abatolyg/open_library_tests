# pages/lists_page.py
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from ..config.config import Config
from ..objects.list import ListObject
from ..objects.list_json_data import ListJsonData
from ..pages.base import BasePage
from ..utils.logger import setup_logger
from ..interfaces.ilist_interface import IList

WEB_LIST_HREF_URL = f"'/people/{Config.WEB_USER}/lists']" 

#Similar to json_list_object there is an option to read logins from the Json FIle or Database
#This time logins are written from the ENV variables just for time limits 
#LoginJsonData
#@pytest.mark.parametrize("json_index", range(len(json_login_objects)))
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
       
        self.BUTTON_LOGIN_LOCATOR = (By.XPATH,"//button[@name='login']")
        self.INPUT_NAME_LOCATOR = (By.NAME,"username")
        self.INPUT_PWD_LOCATOR = (By.NAME,"password")         

    def login(self):

        try:
            self.logger.info("login_page start")
            self.driver.get(Config.WEB_LOGIN_URL)
            self.driver.maximize_window() 
                    
            self.driver.find_element(*self.INPUT_NAME_LOCATOR).send_keys(Config.WEB_LOGIN_EMAIL)
            self.driver.find_element(*self.INPUT_PWD_LOCATOR).send_keys(Config.get_password_decrypted())
            login_button = self.driver.find_element(*self.BUTTON_LOGIN_LOCATOR)
            login_button.click() 

        except NoSuchElementException as e:
            self.logger.error(f"Element not found during login: {e}")
            raise  # Re-raise the exception after logging it

        except TimeoutException as e:
            self.logger.error(f"Timeout occurred during login: {e}")
            raise  # Re-raise the exception after logging it

        except Exception as e:
            self.logger.error(f"An unexpected error occurred during login: {e}")
            raise  # Re-raise the exception after logging it        