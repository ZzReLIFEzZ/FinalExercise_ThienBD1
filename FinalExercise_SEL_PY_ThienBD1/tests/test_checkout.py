from pages.login_page import BaseTest, LoginPage
from pages.inventory_page import IventoryPage
from utils.config_reader import ConfigReader
import random
import time
import allure

class Test_LoginPage(BaseTest):
    @allure.story("Login thành công")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_to_card(self):
        login_page = LoginPage(self.driver)
        iventory_page = IventoryPage(self.driver)
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())
        items = iventory_page.get_inventory_items()  # Ensure inventory items are loaded
        random_index = random.sample(range(len(items)), 3) # Randomly select 3 items to add to cart
        # Add items to cart
        for index in random_index:
            iventory_page.add_item_to_cart(index)
        # Click the cart button to view the cart
        iventory_page.click_cart_button()
        time.sleep(5)   