from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        """Finds an element on the page."""
        return self.driver.find_element(*locator)

    def wait_for_element(self, locator):
        """Waits for an element to be present in the DOM."""
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        return element

    def click(self, locator):
        """Waits for an element to be clickable and then clicks it."""
        element = self.wait_for_element(locator)
        element.click()

    def send_keys(self, locator, keys):
        """Waits for an element to be present and sends keys to it."""
        element = self.wait_for_element(locator)
        element.send_keys(keys)
