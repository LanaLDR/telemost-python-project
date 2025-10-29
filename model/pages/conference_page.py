import allure
from selene import browser, have, be


class ConferencePage:

    def __init__(self):
        self.invalid_session = browser.element('[class^="title_"]')
        self.success_invalid_session_btn = browser.element('[data-test-id="button"]')
        self.welcome_text = browser.element('[class^="waitContinueText_"]')
        self.close_conference_btn = browser.element('[data-test-id="button"][title="Выйти из встречи"]')


    @allure.step("Проверяем наличие сообщения о некорректном номере")
    def should_have_invalid_message(self):
        self.invalid_session.should(have.text("Такой встречи не существует, но вы можете создать новую"))

    @allure.step("Проверяем попадание на встречу")
    def should_open_conference_window(self):
        self.close_conference_btn.should(be.visible)

    @allure.step("Проверяем отображение сообщения о подключении")
    def should_have_welcome_message(self):
        self.welcome_text.should(have.text("Вы подключаетесь к видеовстрече"))