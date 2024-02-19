import pytest
from selenium import webdriver
from configuration import config as path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

driver = None
driver_path = ("C:\z.selenium drivers\chromedriver-win64\chromedriver.exe")
zen_url = ("https://www.zenclass.in/login")

@pytest.fixture(scope="class")
def chrome_driver(request):

    # Setup Chrome driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(zen_url)
    request.cls.driver = zen_url

    yield driver
    # Teardown Chrome driver
    driver.quit()

