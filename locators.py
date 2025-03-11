from selenium.webdriver.common.by import By


class MainPageLocators:
    FAQ_QUESTIONS = [(By.ID, f"accordion__heading-{i}") for i in range(8)]
    FAQ_ANSWERS = [(By.ID, f"accordion__panel-{i}") for i in range(8)]
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[@class='select-search__select']//li[1]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    RENT_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option'][1]")
    COLOR_CHECKBOX_BLACK = (By.XPATH, "//input[@id='black']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Middle')]")
    ACCESS_BUTTON = (By.XPATH, "//button[text()='Да']")


class SuccessPageLocators:
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")