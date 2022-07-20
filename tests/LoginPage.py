import time
from Pages.login import LoginPagePractice


def test_login_page(browser):
    login = LoginPagePractice(browser)

    login.load()
    login.screenshots()
    login.username_password()
    time.sleep(5)
    login.successful_login()
