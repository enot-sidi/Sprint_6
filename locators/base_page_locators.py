from selenium.webdriver.common.by import By
class BasePageLocators:
    SCOOTER_BUTTON_HEADER = (By.CSS_SELECTOR, "[alt='Scooter']")
    YANDEX_BUTTON_HEADER = (By.CSS_SELECTOR, "[alt='Yandex']")
    # Локатор общей кнопки заказа в хедере
    ORDER_BUTTON_HEADER = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')