from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import BaseTest, LoginPage
from utils.config_reader import ConfigReader
from selenium.webdriver.support.ui import WebDriverWait
import allure

class Test_LoginPage(BaseTest):
    @allure.story("Login thành công")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success(self):
        login_page = LoginPage(self.driver)
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())
        # Kiểm tra xem đã đăng nhập thành công chưa
        dashboard_header = self.driver.find_element(By.XPATH, "//div[@class='app_logo']").text
        assert "Swag Labs" in dashboard_header, "Login failed - Swag Labs not found"