from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from urls import Urls


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = None # Должен быть задан в дочерних классах

    def open(self):
        self.driver.get(self.url)

    def fill_input(self, locator, text):
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).send_keys(text)

    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def get_current_url(self): # вернуть текущий url
        return self.driver.current_url

    def switch_to_new_tab_and_wait(self): #
        WebDriverWait(self.driver, 5).until(expected_conditions.number_of_windows_to_be(2))  # Ждем 2 вкладки
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(Urls.redirect_dzen_url))  # Ждём загрузки нужного URL

    def click_order_button(self, locator): # клик по кнопке заказа
        self.scroll_to_element(locator)
        self.click_on_element(locator)

    def is_disappeared(self, locator, timeout=5): # ждет исчезновения элемента
        WebDriverWait(self.driver, timeout,1).until_not(
                expected_conditions.presence_of_element_located(locator))