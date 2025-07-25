from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Call the constructor of BasePage
        self.cart_items = (By.CLASS_NAME, "cart_item")  
        self.checkout_button = (By.ID, "checkout")

    def get_cart_items(self):
        """Returns a list of items in the cart."""
        return self.wait_for_elements(self.cart_items)
    
    def click_checkout_button(self):
        """Clicks the checkout button to proceed with the purchase."""
        return self.click(self.checkout_button)  # Click the checkout button using the click method from BasePage