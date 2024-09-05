import requests
from ..api.base import BaseAPI
from ..config.config import Config
from ..interfaces.ilist_interface import IList
from ..utils.logger import setup_logger

API_CREATE_LIST_URL = f"{Config.BASE_URL}/people/{Config.WEB_USER}/lists"

class ListsAPI(BaseAPI, IList):
    def __init__(self):
        super().__init__()

    #create list and return list key if success, or None if not found  
    def create_list(self, json_list_object):

        ret_val = None

        if self.session_cookie is None:
           self.login_to_openlibrary()

        headers = {
        'Content-Type': 'application/json',
        'Cookie': self.session_cookie
        }

        self.logger.info(f"Creating list: {json_list_object}")
        response = requests.post(API_CREATE_LIST_URL, headers=headers, json=json_list_object)

        if response.status_code == BaseAPI.ERROR_CODE_SUCESS:
            #list_id = response.headers.get('Location') - as appear in documentation, but differ
            #{"key": "/people/anatolyg/lists/OL265809L", "revision": 1}'
            list_key = response.json().get('key')
            self.logger.info(f"List created successfully. key: {list_key}")
            ret_val = list_key
        else:
            self.logger.error(f"Failed to create list. Status code: {response.status_code}")

        return ret_val        
    
    def delete_list(self,list_object):

        ret_val = None 

        if self.session_cookie is None:
           self.login_to_openlibrary()

        #list_id e.g  /people/anatolyg/lists/OL265809L
        #POST /people/anand/list/OL1L/delete.json
        #Content-Type: application/json
        url = f"{Config.BASE_URL}{list_object.key}/delete.json"
        headers = {
        'Content-Type': 'application/json',
        'Cookie': self.session_cookie
        }
       
        self.logger.info(f"Deleting list with ID: {list_object.key}")
        response = requests.post(url, headers=headers)

        if response.status_code == BaseAPI.ERROR_CODE_SUCESS:
            self.logger.info("List deleted successfully")
            ret_val = True
        else:            
            self.logger.error(f"Failed to delete list. Status code: {response.status_code}")

        return ret_val
        
    # Implemented in WEB only for now - login_page, open_lists, open_list_by_key, get_list_name
    # todo this fuction to return all list object and not just name to compare that all json is as sent
    def get_list_object(self,list_object):

        self.logger.error(f"get_list_object not implemented in the API. The only implementation is in the ListPage")
        return None

