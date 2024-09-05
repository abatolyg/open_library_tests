# pages/lists_page.py
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..pages.login import LoginPage
from ..config.config import Config
from ..objects.list import ListObject
from ..objects.list_json_data import ListJsonData
from ..pages.base import BasePage
from ..utils.logger import setup_logger

class ListsDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
       
        self.LIST_DETAILS_TITLE_LOCATOR  = (By.CLASS_NAME,"details-title")        

    def get_list_name(self,list_key):

        self.logger.info("my_list_details")
        # Find the element on detailed page with the class "details-title"
        title_element = self.driver.find_element(*self.LIST_DETAILS_TITLE_LOCATOR)

        json_list_object = ListJsonData()
        json_list_object.set("name", title_element.text)

        list_object = ListObject(list_key, json_list_object.to_json()) 

        self.logger.info("my_list_details")

        return list_object  