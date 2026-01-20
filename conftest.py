import pytest
import logging
from selenium import webdriver

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox',
                     help="Choose browser: chrome or firefox")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("browser")
    driver = None
    
    try:
        if browser == "chrome":
            logging.info("start chrome browser for test..")
            driver = webdriver.Chrome()
        elif browser == "firefox":
            logging.info("start firefox browser for test..")
            driver = webdriver.Firefox()
        else:
            raise pytest.UsageError("--browser should be chrome or firefox")
            
        yield driver
        
    finally:
        logging.info("quit browser..")
        if driver:
            driver.quit()