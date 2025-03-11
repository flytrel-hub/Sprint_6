from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element(driver, locator, time=10):
    return WebDriverWait(driver, time).until(
        EC.presence_of_element_located(locator),
        message=f"Can't find element by locator {locator}"
    )


def click_element(driver, locator, time=10):
    element = WebDriverWait(driver, time).until(
        EC.element_to_be_clickable(locator),
        message=f"Can't click element by locator {locator}"
    )
    element.click()


def get_element_text(driver, locator, time=10):
    element = find_element(driver, locator, time)
    return element.text


def wait_url(driver, URL, time=10):
    return WebDriverWait(driver, time).until(
        EC.url_contains(URL),
        message=f"Can't find URL {URL}"
    )


def scroll_to_element(driver, locator, time=10):
    element = WebDriverWait(driver, time).until(
        EC.presence_of_element_located(locator)
    )
    return driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)