from pages.base_page import BasePage
from locators import MainPageLocators
from urls import BASE_URL
from helpers import click_element, get_element_text, scroll_to_element


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
        self.driver.get(BASE_URL)

    def click_faq_question(self, index):
        scroll_to_element(self.driver, self.locators.FAQ_QUESTIONS[index])
        click_element(self.driver, self.locators.FAQ_QUESTIONS[index])

    def get_faq_answer_text(self, index):
        return get_element_text(self.driver, self.locators.FAQ_ANSWERS[index])

    def click_order_button(self, is_top=True):
        locator = self.locators.ORDER_BUTTON_TOP if is_top else self.locators.ORDER_BUTTON_BOTTOM
        if not is_top:
            scroll_to_element(self.driver, self.locators.ORDER_BUTTON_BOTTOM)
        click_element(self.driver, locator)

    def click_SCOOTER_LOGO(self):
        click_element(self.driver, self.locators.SCOOTER_LOGO)

    def click_YANDEX_LOGO(self):
        click_element(self.driver, self.locators.YANDEX_LOGO)
