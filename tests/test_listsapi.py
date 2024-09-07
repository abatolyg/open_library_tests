# tests/test_listsapi.py
import os
import pytest
import itertools
from ..api.lists import ListsAPI
from ..pages.lists import ListsPage
from ..interfaces.test_strategy_listinterface import TestStrategyListsInterface
from ..utils.test_date_source import CreateListsDataSource, ListStrategiesDataSource
from ..utils.logger import setup_logger

# Log wrtitten to path in env variables 
logger = setup_logger(__name__)

# Load JSON objects from the file or Database - configuration im .env 
json_lists_objects = CreateListsDataSource().get_data()
json_list_strategies = ListStrategiesDataSource().get_data()

# This will create pairs, with None as the fillvalue if one list is shorter
json_data_pairs = itertools.zip_longest(json_lists_objects, json_list_strategies, fillvalue=None)
 
class TestListsAPI:
    @pytest.fixture(scope="function")
    def lists_api(self):
        return ListsAPI()

    @pytest.fixture(scope="function")
    def lists_page(self, driver):
        return ListsPage(driver)
    
    @pytest.mark.parametrize("json_index", range(len(json_lists_objects)), ids=[obj['name'] for obj in json_lists_objects])
    def test_list_create_api_approve_ui_delete_api(self,json_index,lists_api,lists_page):
        """
            Test the list creation, approval, UI interaction, and deletion API.
            Args:
                json_index (int): The index of the JSON object to use for the test.
                lists_api (ListsAPI): An instance of the ListsAPI class.
                lists_page (ListsPage): An instance of the ListsPage class.

            Returns:
                None
            """

        json_lists_object = json_lists_objects[json_index]
        TestStrategyListsInterface().test_list_create_approve_delete(
            json_lists_object,lists_api,lists_page,lists_api)     
    
    @pytest.mark.parametrize("json_data", json_data_pairs)
    def test_list_create_approve_delete_by_List_strategy(self, json_data, lists_api, lists_page):
        """
        Test the create, approve, and delete operations using the List strategy.
        Args:
            json_data: A tuple containing the json_lists_object and json_list_strategy.
            lists_api: An instance of the ListsAPI class.
            lists_page: An instance of the ListsPage class.
        """
        # Unpack the tuple
        json_lists_object, json_list_strategy = json_data
        
        # Handle cases where either is None due to zip_longest OK
        if json_lists_object is None:
            pytest.skip("No corresponding json_lists_object available.")
        
        if json_list_strategy is None:
            pytest.skip("No corresponding json_list_strategy available.")     
   
        # Now you have both json_lists_object and json_list_strategy available
        TestStrategyListsInterface().test_list_create_approve_delete_with_stratey_list(
            json_lists_object,lists_api,lists_page,json_list_strategy)

                 