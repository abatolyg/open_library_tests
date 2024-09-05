# pages/base_page.py
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from ..config.config import Config
from ..utils.logger import setup_logger


#  Page Object Model (POM) is a design pattern 
#  an abstraction layer between the test scripts and the web pages. 
#  It helps organize test code and improve maintainability by separating the page-specific details from the test logic.
#  BasePage is base class for ListsPage and additional classes like BooksPage
#  There are common methods like login_page and close
#  All pages uses driver, logger
class BasePage:
    def __init__(self, driver):
        self.logger = setup_logger(__name__)  # Initialize logger
        self.driver = driver  # Initialize WebDriver instance
        self.logger.info(f"BasePage initialized with driver: {driver}")

    def close(self):

        self.logger.info("close start")
        self.driver.close()

    def find_element(self, locator):
        self.logger.info(f"Finding element: {locator}")
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        self.logger.info(f"Finding elements: {locator}")
        return self.driver.find_elements(*locator)

    def wait_for_element(self, locator, timeout=Config.WAIT_FOR_WEB_ELEMENT_TIMEOUT):
        self.logger.info(f"Waiting for element: {locator}")
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    def wait_for_element(self, locator, timeout=10):
        """Wait for an element to be present on the page"""
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                if self.driver.find_element(*locator):
                    return
            except NoSuchElementException:
                pass
            time.sleep(1)
        raise TimeoutException(f"Element {locator} not found within {timeout} seconds")
