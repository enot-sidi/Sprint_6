import allure
import pytest
from data import Data
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import Urls

class TestLogoNavigation:
    @allure.title("Проверка перехода на главную страницу по клику на логотип 'Самокат'")
    @allure.description(
        "Тест проверяет, что при клике на логотип 'Самокат' на странице заказа происходит перенаправление на главную страницу сайта.")
    def test_click_scooter_logo_redirects_to_main_page(self, driver):# Тест проверяет, что клик на логотип 'Самоката' ведет на главную страницу
        with allure.step("Открытие страницы заказа"):
            page = OrderPage(driver)
            page.open()
        with allure.step("Клик на логотип 'Самокат'"):
            page.click_scooter_logo()
        with allure.step("Получение текущего URL"):
            current_url = page.get_current_url()

        with allure.step(f"Проверка, что URL '{current_url}' равен главной странице '{Urls.main_page_url}'"):
            assert current_url == Urls.main_page_url, f"Ожидалось '{Urls.main_page_url}', но получили '{current_url}'"

    @allure.title("Проверка открытия страницы Дзена по клику на логотип 'Яндекс'")
    @allure.description(
        "Тест проверяет, что при клике на логотип 'Яндекс' открывается главная страница Дзена в новой вкладке через редирект.")
    def test_click_yandex_logo_opens_dzen_in_new_tab(self, driver): # Тест проверяет, что клик на логотип 'Яндекса' открывает главную страницу Дзена в новой вкладке.
        with allure.step("Открытие страницы заказа"):
            page = OrderPage(driver)
            page.open()
        with allure.step("Клик на логотип 'Яндекс'"):
            page.click_yandex_logo()
        with allure.step("Переключение на новую вкладку и ожидание загрузки"):
            page.switch_to_new_tab_and_wait()
        with allure.step("Получение текущего URL"):
            current_url = page.get_current_url()

        with allure.step(f"Проверка, что URL '{current_url}' равен странице Дзена '{Urls.redirect_dzen_url}'"):
            assert current_url == Urls.redirect_dzen_url,  f"Ожидалось '{Urls.redirect_dzen_url}', но получили '{current_url}'"

class TestOrderScooter:
    @pytest.mark.parametrize("order_button, user_data", Data.DATA_ORDER)
    @allure.title("Проверка полного сценария оформления заказа самоката")
    @allure.description(
        "Тест проверяет позитивный сценарий заказа самоката с двумя наборами данных через кнопки 'Заказать' в шапке и на главной странице, включая заполнение форм и подтверждение заказа.")
    def test_order_scooter(self, driver, order_button, user_data):
        """Проверяет оформление заказа при клике на кнопку 'Заказать' в хедере и футере на разных наборах данных через параметризацию """
        with allure.step("Открытие главной страницы"):
            page = MainPage(driver)
            page.open()
        with allure.step(f"Клик на кнопку 'Заказать' с локатором {order_button}"):
            page.click_order_button(order_button)
        with allure.step("Переход на страницу заказа"):
            order_page = OrderPage(driver)
        with allure.step("Заполнение формы 'Для кого самокат'"):
            order_page.fill_form_who_is_scooter(user_data)
        with allure.step("Нажатие кнопки 'Далее'"):
            order_page.click_on_next_button_form()
        with allure.step("Заполнение формы 'Про аренду'"):
            order_page.fill_form_is_rent(user_data)
        with allure.step("Нажатие кнопки 'Заказать' в форме"):
            order_page.click_on_order_button()
        with allure.step("Подтверждение заказа в модальном окне"):
            order_page.confirm_order_in_modal_window()
        with allure.step("Получение текста успешного заказа"):
            success_order_text = order_page.get_text_success_order_status()

        with allure.step(f"Проверка, что текст '{success_order_text}' содержит '{Data.success_order_text}'"):
            assert Data.success_order_text in success_order_text, (
                f"Ожидалось, что сообщение содержит '{Data.success_order_text}', но получили '{success_order_text}'"
            )