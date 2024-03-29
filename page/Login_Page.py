from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.config import BasePage
from page.Home_Page import Home_Page

class Login_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.email = (By.NAME,'email')
        self.password = (By.NAME, 'password')
        self.login_btn = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/button')

    # for Login
    def click_login(self, email_address, passcode):
        self.BasePage.do_send_keys(self.email, email_address)
        self.BasePage.do_send_keys(self.password, passcode)
        self.BasePage.do_clicks(self.login_btn)
        return Home_Page(self.driver)
