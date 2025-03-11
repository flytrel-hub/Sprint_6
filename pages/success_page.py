from pages.base_page import BasePage
from locators import SuccessPageLocators
from helpers import find_element


class SuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SuccessPageLocators()

    def is_order_successful(self):
        return find_element(self.driver, self.locators.SUCCESS_MODAL).is_displayed()