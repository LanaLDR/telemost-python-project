import allure
from selene import browser, be


class MainPage:

    def __init__(self):
        self.join_conference_btn = browser.element('[data-test-id="button"]')
        self.create_conference_btn = browser.element('[data-test-id="create-call-button"]')

    @allure.step("Открываем главную страницу")
    def open(self):
        browser.open("/")

    @allure.step("Кликаем на кнопку подключения к встрече")
    def click_on_join_conference_btn(self):
        self.join_conference_btn.click()

    @allure.step("Кликаем на кнопку создания встречи")
    def click_on_create_conference_btn(self):
        self.create_conference_btn.click()

    @allure.step("Проверяем отображение кнопки главного экрана")
    def should_have_create_conference_btn(self):
        self.create_conference_btn.should(be.visible)