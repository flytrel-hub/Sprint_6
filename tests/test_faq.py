import pytest
import allure
from pages.main_page import MainPage
from data import FAQ_ANSWERS


class TestFAQ:
    @allure.title("Проверка текста в разделе FAQ")
    @allure.description("Проверяем, что при клике на вопрос отображается правильный ответ")
    @pytest.mark.parametrize("index, expected_answer", enumerate(FAQ_ANSWERS))
    def test_faq_answer(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        with allure.step(f"Клик на вопрос {index}"):
            main_page.click_faq_question(index)
        with allure.step(f"Проверка текста ответа для вопроса {index}"):
            actual_answer = main_page.get_faq_answer_text(index)
            assert actual_answer == expected_answer, f"Ответ на вопрос номер {index} отображается неправильно"