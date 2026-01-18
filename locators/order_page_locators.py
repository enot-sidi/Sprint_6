from selenium.webdriver.common.by import By
class OrderPageLocators:
    # Основные поля формы заказа
    TITLE_FORM_ORDER_SCOOTER = (By.XPATH, "//div[text()='Для кого самокат']")  # заголовок формы с данными клиента
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    MONTH_WINDOW = (By.XPATH, '//div[contains(@class, "month-container")]') # окно календаря
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")  # Кнопка "Далее"
    SELECT_FIRST_STATION = (By.XPATH, "//ul/li[1]") # первая станция в выпадающем списке

    # Поля аренды
    TITLE_FORM_ORDER_RENT = (By.XPATH, "//div[text()='Про аренду']")  # заголовок формы с данными аренды
    DELIVERY_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD = (By.CLASS_NAME, 'Dropdown-placeholder')
    RENTAL_OPTION_1_DAY = (By.XPATH, '//div[@class="Dropdown-option" and text()="сутки"]')
    SCOOTER_COLOR_GREY = (By.ID, 'grey')
    COMMENT_COURIER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Order")]/button[text()="Заказать"]')
    ORDER_CONFIRMATION_MODAL_ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "Button") and text() = "Да"]')


    # Окно с подтверждением заказа
    ORDER_CONFIRM_MODAL = (
    By.XPATH, '//div[contains(@class, "ModalHeader") and text() = "Хотите оформить заказ?"]')

    # окно со статусом офрормленого заказа
    ORDER_CONFIRMATION_MODAL_STATUS = (By.XPATH, '//div[contains(@class, "Order") and contains(text(), "Заказ оформлен")]')