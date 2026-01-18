import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox',
                     help="Choose browser: chrome or firefox")
@pytest.fixture
def driver(request):  # создание и закрытие драйвера/браузера
    browser = request.config.getoption("browser")
    driver = None
    if browser == "chrome":
        print("\nstart chrome browser for test..")
        driver  = webdriver.Chrome()
    elif browser == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()