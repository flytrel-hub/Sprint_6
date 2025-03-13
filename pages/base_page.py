from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def click_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Can't click element by locator {locator}"
        )
        element.click()

    def get_element_text(self, locator, time=10):
        element = self.find_element(locator, time)
        return element.text

    def wait_url(self, URL, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.url_contains(URL),
            message=f"Can't find URL {URL}"
        )

    def scroll_to_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)