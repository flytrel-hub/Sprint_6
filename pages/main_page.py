from pages.base_page import BasePage
from locators import MainPageLocators
from urls import BASE_URL


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(BASE_URL)

    def click_faq_question(self, index):
        self.scroll_to_element(MainPageLocators.FAQ_QUESTIONS[index])
        self.click_element(MainPageLocators.FAQ_QUESTIONS[index])

    def get_faq_answer_text(self, index):
        return self.get_element_text(MainPageLocators.FAQ_ANSWERS[index])

    def click_order_button(self, is_top=True):
        locator = MainPageLocators.ORDER_BUTTON_TOP if is_top else MainPageLocators.ORDER_BUTTON_BOTTOM
        if not is_top:
            self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(locator)

    def click_SCOOTER_LOGO(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_YANDEX_LOGO(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)