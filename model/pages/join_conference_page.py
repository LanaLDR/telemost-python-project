import allure
from selene import browser, have


class JoinConferencePage:

    def __init__(self):
        self.conference_id_input = browser.element('.Textinput-Control')
        self.join_conference_btn = browser.element('[data-test-id="button"]')
        self.close_join_conference_btn = browser.element('[data-test-id="button"][aria-label="Закрыть окно"]')

    @allure.step("Открываем страницу подключения к встрече")
    def open(self):
        browser.open("/connect-to-meeting-by-id")

    @allure.step("Вводим номер встречи {conference_id}")
    def fill_conference_id(self, conference_id):
        self.conference_id_input.set(conference_id)

    @allure.step("Кликаем на кнопку 'Подключиться'")
    def click_on_join_conference_btn(self):
        self.join_conference_btn.click()

    @allure.step("Кликаем на кнопку закрытия окна подключения")
    def click_on_close_join_conference_btn(self):
        self.close_join_conference_btn.click()

    @allure.step("Проверяем, что значение в инпуте осталось пустым")
    def should_have_empty_value_in_conference_id_input(self):
        self.conference_id_input.should(have.value(""))