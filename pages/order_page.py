import urls
from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.Urls.order_page_url
        self.locators = OrderPageLocators()
        self.locators_base = BasePageLocators()

    def click_yandex_logo(self):  # клик по лого яндекса в хедере
        self.click_on_element(self.locators_base.YANDEX_BUTTON_HEADER)

    def click_scooter_logo(self): # клик на лого самоката в хедере
        self.click_on_element(self.locators_base.SCOOTER_BUTTON_HEADER)

    def wait_form_who_is_scooter(self): # ждем форму с данными клиента
        self.wait_visibility_of_element(self.locators.TITLE_FORM_ORDER_SCOOTER)

    def wait_form_rent(self): # ждем формы с данными по аренде
        self.wait_visibility_of_element(self.locators.TITLE_FORM_ORDER_RENT)


    def fill_form_who_is_scooter(self, user_data): # Заполнение формы
        self.wait_form_who_is_scooter()
        # заполнили имя/фамилию/адрес/номер
        self.fill_input(self.locators.FIRST_NAME, user_data['first_name'])
        self.fill_input(self.locators.LAST_NAME, user_data['last_name'])
        self.fill_input(self.locators.ADDRESS, user_data['address'])
        self.fill_input(self.locators.PHONE, user_data['phone_number'])
        # выбрали первую станцию
        self.click_on_element(self.locators.METRO_STATION)
        self.click_on_element(self.locators.SELECT_FIRST_STATION)

    def click_on_next_button_form(self):
            self.click_on_element(self.locators.NEXT_BUTTON)

    def fill_form_is_rent(self, user_data):
        self.wait_form_rent()
        self.fill_input(self.locators.DELIVERY_DATE, user_data['rental_date'])
        self.click_on_element(self.locators.TITLE_FORM_ORDER_RENT) # клик для закрытия календаря
        self.is_disappeared(self.locators.MONTH_WINDOW) # ждем закрытия календаря
        self.click_on_element(self.locators.RENTAL_PERIOD)
        self.click_on_element(self.locators.RENTAL_OPTION_1_DAY)
        self.click_on_element(self.locators.SCOOTER_COLOR_GREY)
        self.fill_input(self.locators.COMMENT_COURIER, user_data['comment_courier'])

    def click_on_order_button(self):
        self.click_on_element(self.locators.ORDER_BUTTON)


    def confirm_order_in_modal_window(self): # подтверждение оформления заказа
        self.wait_visibility_of_element(self.locators.ORDER_CONFIRM_MODAL)
        self.click_on_element(self.locators.ORDER_CONFIRMATION_MODAL_ORDER_BUTTON)

    def get_text_success_order_status(self): # ждем появления окна с успешным заказом
        self.wait_visibility_of_element(self.locators.ORDER_CONFIRMATION_MODAL_STATUS)
        return self.get_text_element(self.locators.ORDER_CONFIRMATION_MODAL_STATUS)