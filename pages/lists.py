# pages/lists_page.py
from ..pages.list_details import ListsDetailsPage
from ..pages.login import LoginPage
from ..config.config import Config
from ..objects.list import ListObject
from ..objects.list_json_data import ListJsonData
from ..pages.base import BasePage
from ..utils.logger import setup_logger
from ..interfaces.ilist_interface import IList
from selenium.webdriver.common.by import By

WEB_LIST_HREF_URL = f"'/people/{Config.WEB_USER}/lists']" 

class ListsPage(BasePage, IList):
    def __init__(self, driver):
        super().__init__(driver)
       
        self.BUTTON_LOGIN_LOCATOR = (By.XPATH,"//button[@name='login']")
        self.INPUT_NAME_LOCATOR = (By.NAME,"username")
        self.INPUT_PWD_LOCATOR = (By.NAME,"password")         
        self.LIST_DETAILS_TITLE_LOCATOR  = (By.CLASS_NAME,"details-title")        

    # login_page, open_lists, open_list_by_key, get_list_name
    # todo this fuction to return all list object and not just name to compare that all json is as sent
    def get_list_object(self,list_object):

        list_object_ret_val = None

        loginPage = LoginPage(self.driver)

        loginPage.login()

        # this should be LoginPage 
        self.__open_lists()

        self.__open_list_by_key(list_object.key)

        listsDetailsPage = ListsDetailsPage(self.driver)

        list_object_ret_val = listsDetailsPage.get_list_name(list_object.key)

        self.close()    

        return list_object_ret_val   

    #create list and return list key if success, or None if not found  
    def create_list(self, json_list_object):
        
        self.logger.info("create_list not implemented in Page for now. Only in ListAPI")
        return None
    
    def delete_list(self,list_object):

        self.logger.info("delete_list not implemented in Page for now. Only in ListAPI")
        return None    

    def __open_lists(self):

        self.logger.info("press_my_lists start")
        href = "//a[@href=" + WEB_LIST_HREF_URL
        href_see_all_element = self.driver.find_element(By.XPATH,href) 
        href_see_all_element.click()

    def __open_list_by_key(self, list_key):
        
        self.logger.info("my_list_details")
        href = "//a[@href='" + list_key + "']"
        href_list_by_key = self.driver.find_element(By.XPATH,href )
        href_list_by_key.click()

    def __get_list_name(self,list_key):

        self.logger.info("my_list_details")
        # Find the element on detailed page with the class "details-title"
        title_element = self.driver.find_element(*self.LIST_DETAILS_TITLE_LOCATOR)

        json_list_object = ListJsonData()
        json_list_object.set("name", title_element.text)

        list_object = ListObject(list_key, json_list_object.to_json()) 

        self.logger.info("my_list_details")

        return list_object  