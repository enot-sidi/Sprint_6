import urls
from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
import allure

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.Urls.order_page_url
        self.locators = OrderPageLocators()
        self.locators_base = BasePageLocators()

    @allure.step("Клик по логотипу Яндекса в хедере")
    def click_yandex_logo(self):
        self.click_on_element(self.locators_base.YANDEX_BUTTON_HEADER)

    @allure.step("Клик по логотипу Самоката в хедере")
    def click_scooter_logo(self):
        self.click_on_element(self.locators_base.SCOOTER_BUTTON_HEADER)

    @allure.step("Ожидание появления формы для клиента")
    def wait_form_who_is_scooter(self):
        self.wait_visibility_of_element(self.locators.TITLE_FORM_ORDER_SCOOTER)

    @allure.step("Ожидание появления формы аренды")
    def wait_form_rent(self):
        self.wait_visibility_of_element(self.locators.TITLE_FORM_ORDER_RENT)

    @allure.step("Заполнение формы данных клиента")
    def fill_form_who_is_scooter(self, user_data):
        self.wait_form_who_is_scooter()
        
        # Заполнение основных полей
        self.fill_input(self.locators.FIRST_NAME, user_data['first_name'])
        self.fill_input(self.locators.LAST_NAME, user_data['last_name'])
        self.fill_input(self.locators.ADDRESS, user_data['address'])
        self.fill_input(self.locators.PHONE, user_data['phone_number'])
        
        # Выбор станции метро
        self.click_on_element(self.locators.METRO_STATION)
        self.click_on_element(self.locators.METRO_STATION_OPTION)

    @allure.step("Клик по кнопке 'Далее' в форме")
    def click_on_next_button_form(self):
        self.click_on_element(self.locators.NEXT_BUTTON)

    @allure.step("Заполнение формы аренды")
    def fill_form_is_rent(self, user_data):
        self.wait_form_rent()
        
        # Заполнение даты доставки
        self.fill_input(self.locators.DELIVERY_DATE, user_data['rental_date'])
        self.click_on_element(self.locators.TITLE_FORM_ORDER_RENT)  # Закрытие календаря
        self.is_disappeared(self.locators.MONTH_WINDOW)
        
        # Выбор параметров аренды
        self.click_on_element(self.locators.RENTAL_PERIOD)
        self.click_on_element(self.locators.RENTAL_OPTION_1_DAY)
        self.click_on_element(self.locators.SCOOTER_COLOR_GREY)
        
        # Комментарий для курьера
        self.fill_input(self.locators.COMMENT_COURIER, user_data['comment_courier'])

    @allure.step("Клик по кнопке 'Заказать'")
    def click_on_order_button(self):
        self.click_on_element(self.locators.ORDER_BUTTON)

    @allure.step("Подтверждение заказа в модальном окне")
    def confirm_order_in_modal_window(self):
        self.wait_visibility_of_element(self.locators.ORDER_CONFIRM_MODAL)
        self.click_on_element(self.locators.ORDER_CONFIRMATION_MODAL_ORDER_BUTTON)

    @allure.step("Получение текста статуса успешного заказа")
    def get_text_success_order_status(self):
        self.wait_visibility_of_element(self.locators.ORDER_CONFIRMATION_MODAL_STATUS)
        return self.get_text_element(self.locators.ORDER_CONFIRMATION_MODAL_STATUS)