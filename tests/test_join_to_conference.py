import allure

from Application import app
from data.conferences_id import ids

@allure.title("Подключение с некорректным номером")
def test_join_with_invalid_number(setup_browser):
    app.main_page.open()
    app.main_page.click_on_join_conference_btn()
    app.join_conference_page.fill_conference_id(ids.invalid_number)
    app.join_conference_page.click_on_create_conference_btn()
    app.conference_page.should_have_invalid_message()

@allure.title("Подключение с корректным номером")
def test_join_with_correct_number(setup_browser):
    app.main_page.open()
    app.main_page.click_on_join_conference_btn()
    app.join_conference_page.fill_conference_id(ids.correct_number)
    app.join_conference_page.click_on_create_conference_btn()
    app.conference_page.should_have_welcome_message()

@allure.title("Закрытие окна подключения")
def test_close_join_page(setup_browser):
    app.main_page.open()
    app.main_page.click_on_join_conference_btn()
    app.join_conference_page.click_on_close_join_conference_btn()
    app.main_page.should_have_create_conference_btn()

@allure.title("Ввод не численных значений в инпут номера конференции")
def test_fill_not_int_in_conference_number(setup_browser):
    app.main_page.open()
    app.main_page.click_on_join_conference_btn()
    app.join_conference_page.fill_conference_id(ids.invalid_not_int_number)
    app.join_conference_page.should_have_empty_value_in_conference_id_input()

@allure.title("Подключение с пустым номером")
def test_join_with_empty_number(setup_browser):
    app.main_page.open()
    app.main_page.click_on_join_conference_btn()
    app.join_conference_page.click_on_create_conference_btn()
    app.join_conference_page.should_have_empty_value_in_conference_id_input()