import urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.Urls.main_page_url
        self.locators = MainPageLocators()

    def click_on_question_in_faq(self, question_locator):
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)

    def get_answer_text_in_faq(self, answer_locator):
        self.wait_visibility_of_element(answer_locator)
        answer = self.get_text_element(answer_locator)
        return answer