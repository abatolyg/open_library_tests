Consider the following site: https://openlibrary.org
Write automation tests for the  lists api, using Python, Pytest and POM:
1. Create a list via api
2. Approve that the list exists via UI
3. Delete the list via api
4. Description.Test Project QA Automation for OpenLibrary (Pytest, Selenium, RestAPI)

Video introduction in Hebrew is here: https://drive.google.com/drive/folders/1TX07rSlt8yoNiqi0BteW0nbbWNlSRxzA

.env   - Environment Variables

WEB_PASSWORD_ENCRYPTED=gAAAAABm1v3lEtrRW2TjWcsyoo
WEB_LOGIN_EMAIL=anatolyg@gmail.com
API_LOGIN_ACCESS=UQRbDYVkNyeGa8Vw
API_LOGIN_SECRET=XgqOHGMyS5XMsGba
BASE_URL=https://openlibrary.org
BROWSER=chrome
HEADLESS=false
WAIT_FOR_WEB_ELEMENT_TIMEOUT=10
TEST_DATA_FILE_PATH = testsdata/test_data.json
TEST_DATA_SOURCE_TYPE=file
#DATA_SOURCE_TYPE=database
LOG_FILE_PATH=C:\logs\automation.log

Details

1. Test Name: test_create_approve_and_delete_list
2. The same test is executed with different parameters several times using  pytest.mark.parametrize
 @pytest.mark.parametrize("json_index", range(len(json_lists_objects)))
 def test_create_approve_and_delete_list(self,json_index,lists_api,lists_page):
3. Test Parameters: json_lists_objects - taken from TEST_DATA_SOURCE
4. TEST_DATA_SOURCE_TYPE:file / or database
5. TEST_DATA_FILE_PATH default: testsdata/test_data.json
DataSource class implements a Singleton Design pattern - 
return JSON data either from a file or from a database’ based on configuration.
6. Json_lists_objects are passed to the test_create_approve_and_delete_list
Test_data.json file example
[
    {
        "name": "18th Century Architecture for Melisa",
        "description": "Studies of architectural practice,mainly English",
        "tags": ["Architecture", "18th Century", "Drawings", "Buildings"],
        "seeds": [
            "/books/OL1M",
            "/subjects/gothic_architecture"
        ]
    },
    {
        "name": "19th Century Architecture for Lynda",
        "description": "Architectural evolution during the 19th Europe",
        "tags": ["Architecture", "19th Century", "Drawings", "Buildings"],
        "seeds": [
            "/books/OL2M",
            "/subjects/neo_gothic_architecture"
        ]
    }
]
7. The Strategy Pattern is a behavioral design pattern that enables selecting an algorithm's behavior at runtime.
This allows us to build different test strategies based on the same functionality. 
The Test Person chooses which strategy to use without knowing the details of the implementation.
API and WEB interfaces implements interface IList with 3 methods: 
create_list with 
approve_list_created
delete_list
This separation allows also to replace implementation and no need to change the test - decoupling: SELENIUM can be replaced by Playwright, HTTP Client can be  replace by REST 
8. Page Object Model (POM) design pattern used
Abstraction layer between the test scripts and the web pages.
It helps organize test code and improve maintainability by separating the page-specific details from the test logic.
BasePage is base class for ListsPage and additional classes like BooksPage  in the future
There are common methods like login_page and close
All pages uses driver, logger
BaseAPI is base class for ListsAPI and additional classes like BooksAPI in the future
All API uses Login functionality derived from base. 
9. Logger - write logs to file 
PasswordManager encrypt_password and decrypt_password not to store plaintext 
10. How to run tests
Option 1: From Visual Studio Code  - see picture below
Option 2: cd to techsee\open_library_test and run  pytest  - see picture below
