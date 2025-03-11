from pages.base_page import BasePage
from locators import OrderPageLocators
from helpers import find_element, click_element


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def fill_first_form(self, name, surname, address, metro, phone):
        find_element(self.driver, self.locators.NAME_INPUT).send_keys(name)
        find_element(self.driver, self.locators.SURNAME_INPUT).send_keys(surname)
        find_element(self.driver, self.locators.ADRESS_INPUT).send_keys(address)
        metro_field = find_element(self.driver, self.locators.METRO_INPUT)
        metro_field.click()
        metro_field.send_keys(metro)
        click_element(self.driver, self.locators.METRO_OPTION)
        find_element(self.driver, self.locators.PHONE_INPUT).send_keys(phone)
        click_element(self.driver, self.locators.NEXT_BUTTON)

    def fill_second_form(self, date, rent_period, color, comment):
        find_element(self.driver, self.locators.DATE_INPUT).send_keys(date)
        click_element(self.driver, self.locators.COLOR_CHECKBOX_BLACK)
        click_element(self.driver, self.locators.RENT_PERIOD_DROPDOWN)
        click_element(self.driver, self.locators.RENT_PERIOD_OPTION)
        find_element(self.driver, self.locators.COMMENT_INPUT).send_keys(comment)
        click_element(self.driver, self.locators.SUBMIT_BUTTON)
        click_element(self.driver, self.locators.ACCESS_BUTTON)

