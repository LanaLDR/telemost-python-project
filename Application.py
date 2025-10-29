from model.pages.conference_page import ConferencePage
from model.pages.join_conference_page import JoinConferencePage
from model.pages.main_page import MainPage


class Application:
    def __init__(self):
        self.main_page = MainPage()
        self.join_conference_page = JoinConferencePage()
        self.conference_page = ConferencePage()


app = Application()