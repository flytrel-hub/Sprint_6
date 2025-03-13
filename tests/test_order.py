import pytest
import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.success_page import SuccessPage
from data import order_data
from urls import BASE_URL, DZEN_URL


class TestOrder:
    @allure.title("Проверка процесса заказа самоката")
    @allure.description("Проверяем полный позитивный сценарий заказа с двумя наборами данных и двумя точками входа")
    @pytest.mark.parametrize("order", order_data)
    @pytest.mark.parametrize("is_top_button", [True, False])
    def test_order_flow(self, driver, order, is_top_button):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        success_page = SuccessPage(driver)

        with allure.step(f"Клик на кнопку 'Заказать' (верхняя: {is_top_button})"):
            main_page.click_order_button(is_top_button)
        with allure.step("Заполнение первой формы заказа"):
            order_page.fill_first_form(
                order["name"], order["surname"], order["address"],
                order["metro"], order["phone"]
            )
        with allure.step("Заполнение второй формы заказа"):
            order_page.fill_second_form(
                order["date"], order["rent_period"], order["color"], order["comment"]
            )
        with allure.step("Проверка успешного оформления заказа"):
            assert success_page.is_order_successful(), "Заказ не оформлен"

    @allure.title("Проверка редиректа по логотипу Самоката")
    @allure.description("Проверяем, что клик на логотип Самоката возвращает на главную страницу")
    def test_SCOOTER_LOGO_redirect(self, driver):
        main_page = MainPage(driver)
        with allure.step("Клик на кнопку 'Заказать'"):
            main_page.click_order_button()
        with allure.step("Клик на логотип Самоката"):
            main_page.click_SCOOTER_LOGO()
        with allure.step("Проверка URL главной страницы"):
            assert BASE_URL in driver.current_url, "Нет редиректа на главную страницу"

    @allure.title("Проверка редиректа по логотипу Яндекса")
    @allure.description("Проверяем, что клик на логотип Яндекса открывает Дзен в новом окне")
    def test_YANDEX_LOGO_redirect(self, driver):
        main_page = MainPage(driver)
        with allure.step("Клик на логотип Яндекса"):
            main_page.click_YANDEX_LOGO()
        with allure.step("Переключение на новое окно"):
            driver.switch_to.window(driver.window_handles[1])
        with allure.step("Ожидание полной загрузки страницы и изменения URL"):
            base_page = BasePage(driver)
            base_page.wait_url(DZEN_URL)
        with allure.step("Проверка URL Дзена"):
            assert DZEN_URL in driver.current_url, "Нет редиректа на страницу Дзена"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
