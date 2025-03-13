from pages.base_page import BasePage
from locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_first_form(self, name, surname, address, metro, phone):
        self.find_element(OrderPageLocators.NAME_INPUT).send_keys(name)
        self.find_element(OrderPageLocators.SURNAME_INPUT).send_keys(surname)
        self.find_element(OrderPageLocators.ADRESS_INPUT).send_keys(address)
        metro_field = self.find_element(OrderPageLocators.METRO_INPUT)
        metro_field.click()
        metro_field.send_keys(metro)
        self.click_element(OrderPageLocators.METRO_OPTION)
        self.find_element(OrderPageLocators.PHONE_INPUT).send_keys(phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def fill_second_form(self, date, rent_period, color, comment):
        self.find_element(OrderPageLocators.DATE_INPUT).send_keys(date)
        self.click_element(OrderPageLocators.COLOR_CHECKBOX_BLACK)
        self.click_element(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click_element(OrderPageLocators.RENT_PERIOD_OPTION)
        self.find_element(OrderPageLocators.COMMENT_INPUT).send_keys(comment)
        self.click_element(OrderPageLocators.SUBMIT_BUTTON)
        self.click_element(OrderPageLocators.ACCESS_BUTTON)

