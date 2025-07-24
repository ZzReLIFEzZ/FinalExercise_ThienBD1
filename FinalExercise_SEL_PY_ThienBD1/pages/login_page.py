from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from base.base_test import BaseTest
from base.base_page import BasePage
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Call the constructor of BasePage
        self.username_field = (By.NAME, "user-name") # Assuming the username field has a name attribute "username"
        self.password_field = (By.NAME, "password") # Assuming the password field has a name attribute "password"
        self.login_button = (By.XPATH, "//*[@id='login-button']") # Assuming the login button is a submit button


    def do_login(self, username, password):
        self.enter_username(username) # Enter the username
        self.enter_password(password) # Enter the password       
        self.click_login_button()     # Click the login button
        time.sleep(5)                # Wait for 10 seconds to observe the result (not recommended for production code)
    
    def enter_username(self, username):
        username_element = self.wait_for_element(self.username_field) # Wait for the username field to be present
        username_element.send_keys(username) # Enter the username using the send_keys method from BasePage

    def enter_password(self, password):
        password_element = self.wait_for_element(self.password_field) # Wait for the password field to be present
        password_element.send_keys(password) # Enter the password using the send_keys method from BasePage

    def click_login_button(self):
        self.click(self.login_button) # Click the login button using the click method from BasePage