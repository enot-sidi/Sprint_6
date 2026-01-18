import allure
import pytest
from data import Data
from pages.main_page import MainPage



class TestFAQDropdown:
    """Проверяет, что при клике на вопрос отображается правильный текст ответа."""
    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", Data.FAQ_DATA)
    @allure.title("Проверка раскрытия ответа на вопрос в разделе FAQ")
    @allure.description(
        "Тест проверяет, что при клике на каждый вопрос в разделе 'Вопросы о важном' отображается соответствующий текст ответа.")
    def test_click_faq_question_expands_correct_answer(self, driver, question_locator, answer_locator, expected_text):
        with allure.step("Открытие главной страницы"):
            page = MainPage(driver)
            page.open()
        with allure.step(f"Клик на вопрос с локатором {question_locator}"):
            page.click_on_question_in_faq(question_locator)
        with allure.step(f"Получение текста ответа с локатором {answer_locator}"):
            actual_text = page.get_answer_text_in_faq(answer_locator)

        with allure.step(f"Проверка, что текст ответа '{actual_text}' соответствует ожидаемому '{expected_text}'"):
            assert actual_text == expected_text, f"Ожидалось '{expected_text}', но получили '{actual_text}'"
            