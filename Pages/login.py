import json
from selenium.webdriver.common.by import By


class LoginPagePractice:
    with open('D:/automationProjects/pytest_login/config.json') as config_file:
        config = json.load(config_file)

    url = "https://rahulshettyacademy.com/locatorspractice/"
    username = (By.ID, config['username'])
    password = (By.NAME, config['password'])
    first_check = (By.ID, config['firstcheckbox'])
    second_check = (By.ID, config['secondcheckbox'])
    button = (By.CLASS_NAME, config['signIn'])
    LogOutBtn = (By.CLASS_NAME, config['logout'])

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url)

    def username_password(self):
        self.browser.find_element(*self.username).send_keys(self.config['name'])
        self.browser.find_element(*self.password).send_keys(self.config['pass'])
        self.browser.find_element(*self.first_check).click()
        self.browser.find_element(*self.second_check).click()
        self.browser.find_element(*self.button).click()

    def successful_login(self):
        assert self.browser.find_element(*self.LogOutBtn).is_displayed()
        self.browser.find_element(*self.LogOutBtn).click()

    def screenshots(self):
        self.browser.save_screenshot("D:\\automationProjects\\pytest_login\\screenshots\\LoginPage.png")
