import pytest
import allure

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    # Настройка Firefox для отображения окна
    firefox_options = Options()
    firefox_options.headless = False  # Отключаем headless-режим (окно видно)
    driver = webdriver.Firefox(options=firefox_options)

    # Привязка драйвера к отчету Allure
    allure.attach(driver.get_screenshot_as_png(), name="Browser Screenshot", attachment_type=allure.attachment_type.PNG)
    yield driver
    driver.quit()
