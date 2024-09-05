from ..objects.list import ListObject
from ..utils.logger import setup_logger

logger = setup_logger(__name__)

# The Strategy Pattern is a behavioral design pattern that enables selecting an algorithm's behavior at runtime. 
# This pattern defines a family of algorithms, encapsulates each one as a separate class, and makes them interchangeable. 
# The client chooses which strategy to use without knowing the details of the implementation
# client only select API or WEB.
# This allow to build different test strategies based on the same functionality. 
#     create_list with API/WEB, approve_list_created API/WEB, delete_list API/WEB
# This allows to replace implementation and no need to change the test - decopling 
# SELEIUM to Playwright, HTTP Cleint to replace with REST API
class TestStrategyListsInterface:

    def __init__(self):
        super().__init__()

    def  test_list_create_approve_delete(self,json_lists_object,icreate,iappove,idelete):

        logger.info("===Test started. create, approve, and delete list. ")

        # 1. Create list by REST api using HTTP Client Post
        created_list_object = self.create_list(icreate,json_lists_object)
        
        # 2. Approve that the list exists via UI using selenium navigation and retrieve list object information
        self.approve_list_created(iappove,created_list_object)

        # 3. Delete list created in previous step by API call using key 
        self.delete_list(idelete,created_list_object)   

        logger.info("===Test completed. create, approve, and delete list")        

    def  test_list_create_approve_delete_with_stratey_list(self,json_lists_object,lists_api,lists_page,json_list_strategy):        
     
        logger.info("===Test started. create, approve, and delete list")           
        
        operations = {"create": lists_api,"approve": lists_api,"delete": lists_api}

        for operation, default in operations.items():
            if json_list_strategy.get(operation) == "lists_page":
                operations[operation] = lists_page

        self.test_list_create_approve_delete(
            json_lists_object,
            operations["create"],
            operations["approve"],
            operations["delete"]
        )

        logger.info("===Test completed. create, approve, and delete list")

    def create_list(self,lists_interface,json_lists_object):
           
        # 1. create_list via lists_interface
        list_key = lists_interface.create_list(json_lists_object)
        assert list_key, "Failed to create list {json_lists_object}"

        list_object = ListObject(list_key,json_lists_object)        

        logger.info("==== Task 1 Completed. List created successfully by API")   

        return list_object
        
    def approve_list_created(self, lists_interface, list_object):

        # 2. approve_list_created via lists_interface
        list_object_ret_val = lists_interface.get_list_object(list_object)  

        list_name_expected = list_object.json_list_object.get("name")    
        list_name_returned = list_object_ret_val.json_list_object.get("name")    

        # Assert to check if the actual output matches the expected output
        assert list_name_expected == list_name_returned, f"Expected '{list_name_expected}' but got '{list_name_returned}'" 

        logger.info("==== Task 2 Completed. approve_list_created_by_ui")

    def delete_list(self, lists_interface, list_object):

         # 3. delete_list via lists_interface
        success = lists_interface.delete_list(list_object)
        assert success, f"Failed to delete list with ID {list_object.key}"
        
        logger.info("==== Task 3 Completed. delete_list_by_api")