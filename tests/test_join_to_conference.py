from Application import app
from data.conferences_id import Ids


def test_join_with_invalid_number(setup_browser):
    app.main_page.open()
    app.main_page.click_on_join_conference_btn()
    app.join_conference_page.fill_conference_id(Ids.invalid_number)
    app.join_conference_page.click_on_join_conference_btn()
    app.conference_page.should_have_invalid_message()

def test_join_with_correct_number(setup_browser):
    app.main_page.open()
    app.main_page.click_on_join_conference_btn()
    app.join_conference_page.fill_conference_id(Ids.correct_number)
    app.join_conference_page.click_on_join_conference_btn()
    app.conference_page.should_have_welcome_message()

def test_close_join_page(setup_browser):
    app.main_page.open()
    app.main_page.click_on_join_conference_btn()
    app.join_conference_page.click_on_close_join_conference_btn()
    app.main_page.should_have_create_conference_btn()

def test_fill_not_int_in_conference_number(setup_browser):
    app.main_page.open()
    app.main_page.click_on_join_conference_btn()
    app.join_conference_page.fill_conference_id(Ids.invalid_not_int_number)
    app.join_conference_page.should_have_empty_value_in_conference_id_input()

def test_join_with_empty_number(setup_browser):
    app.main_page.open()
    app.main_page.click_on_join_conference_btn()
    app.join_conference_page.click_on_join_conference_btn()
    app.join_conference_page.should_have_empty_value_in_conference_id_input()