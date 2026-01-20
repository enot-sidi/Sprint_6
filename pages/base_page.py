import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from urls import Urls

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = None  # Должен быть задан в дочерних классах

    @allure.step("Открытие страницы")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Заполнение поля ввода")
    def fill_input(self, locator, text):
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step("Ожидание видимости элемента")
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Клик по элементу")
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step("Получение текста элемента")
    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Прокрутка к элементу")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_tab_and_wait(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.number_of_windows_to_be(2))  # Ждем 2 вкладки
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(Urls.redirect_dzen_url))  # Ждём загрузки нужного URL

    @allure.step("Клик по кнопке заказа")
    def click_order_button(self, locator):
        self.scroll_to_element(locator)
        self.click_on_element(locator)

    @allure.step("Ожидание исчезновения элемента")
    def is_disappeared(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout, 1).until_not(
            expected_conditions.presence_of_element_located(locator))