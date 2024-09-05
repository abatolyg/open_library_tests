# tests/conftest.py - do not move this file 
# conftest.py is used to share fixtures across tests. 
# Fixtures defined in conftest.py are available to all test files within the same directory and its subdirectories.
import os
from urllib import request
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ..utils.logger import setup_logger
from ..config.config import Config

logger = setup_logger(__name__)

def get_driver_with_param(browser):
    if browser == "chrome":
        service = Service(ChromeDriverManager(version="latest").install())
        options = webdriver.ChromeOptions()
        if Config.HEADLESS:
            options.add_argument("--headless")
        return webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        service = Service(GeckoDriverManager(version="latest").install())
        options = webdriver.FirefoxOptions()
        if Config.HEADLESS:
            options.add_argument("--headless")
        return webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {Config.BROWSER}")
   
#Scope function and not session - new WebDriver instance at the start of each test function and properly quit it after the test is complete.
@pytest.fixture(params=["chrome", "firefox"],scope="function")
def driver(request):
    logger.info(f"Initializing {request.param} driver")
    driver = get_driver_with_param(request.param)
    driver.implicitly_wait(Config.WAIT_FOR_WEB_ELEMENT_TIMEOUT)
    yield driver
    logger.info("Quitting driver")
    driver.quit()
