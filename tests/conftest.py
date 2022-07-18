import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():

    b = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    yield b

    b.implicitly_wait(10)
