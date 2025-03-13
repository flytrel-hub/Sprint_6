from pages.base_page import BasePage
from locators import SuccessPageLocators


class SuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_order_successful(self):
        return self.find_element(SuccessPageLocators.SUCCESS_MODAL).is_displayed()