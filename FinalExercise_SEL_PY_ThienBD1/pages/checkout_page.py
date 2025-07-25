from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Call the constructor of BasePage
        self.first_name_field = (By.NAME, "firstName")
        self.last_name_field = (By.NAME, "lastName")
        self.postal_code_field = (By.NAME, "postalCode")
        self.continue_button = (By.ID, "continue")
        self.cancel_button = (By.ID, "cancel")
        self.finish_button = (By.ID, "finish")

    def enter_first_name(self, first_name):
        """Enters the first name in the checkout form."""
        first_name_element = self.wait_for_element(self.first_name_field)
        first_name_element.send_keys(first_name)

    def enter_last_name(self, last_name):
        """Enters the last name in the checkout form."""
        last_name_element = self.wait_for_element(self.last_name_field)
        last_name_element.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        """Enters the postal code in the checkout form."""
        postal_code_element = self.wait_for_element(self.postal_code_field)
        postal_code_element.send_keys(postal_code)

    def click_continue_button(self):
        """Clicks the continue button to proceed with the checkout."""
        self.click(self.continue_button)

    def click_cancel_button(self):
        """Clicks the cancel button to go back to the cart."""
        self.click(self.cancel_button)

    def click_finish_button(self):
        """Clicks the finish button to complete the checkout."""
        self.click(self.finish_button)

    def do_checkout(self, first_name, last_name, postal_code):
        """Performs the checkout process by entering details and clicking continue."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue_button()
        # Optionally, you can add a wait here to ensure the next page loads