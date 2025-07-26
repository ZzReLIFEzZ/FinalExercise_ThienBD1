from pages.login_page import BaseTest, LoginPage
from pages.inventory_page import IventoryPage
from pages.cart_page import CartPage as Cart_Page
from pages.checkout_page import CheckoutPage
from utils.config_reader import ConfigReader
from selenium.webdriver.common.by import By
import random
import time
import allure

class Test_CheckoutPage(BaseTest):
    @allure.story("Mua hàng thành công")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_purchase_successful(self):
        """Test to add items to the cart and complete the checkout process."""
        login_page = LoginPage(self.driver)
        iventory_page = IventoryPage(self.driver)
        cart_page = Cart_Page(self.driver)
        checkout_page = CheckoutPage(self.driver)
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password()) # Đăng nhập vào trang web
        items = iventory_page.get_inventory_items() # Lây danh sách các sản phẩm trong kho
        random_index = random.sample(range(len(items)), 3) # Lấy ngẫu nhiên 3 sản phẩm từ kho
        # Add items to cart
        for index in random_index:
            iventory_page.add_item_to_cart(index)   # Thêm sản phẩm vào giỏ hàng
        iventory_page.click_cart_button()   # Click vào giỏ hàng để xem các sản phẩm đã thêm
        cart_page.click_checkout_button()   # Click vào nút checkout để tiến hành thanh toán
        checkout_page. do_checkout(
            ConfigReader.get_firstname(),
            ConfigReader.get_lastname(),
            ConfigReader.get_zipcode()
        )   # Điền thông tin thanh toán
        checkout_page.click_finish_button() # Click vào nút finish để hoàn tất thanh toán
        # Kiểm tra xem đã hoàn tất thanh toán thành công chưa
        confirmation_message = self.driver.find_element(By.XPATH, "//h2[@class='complete-header']").text
        assert "Thank you for your order!" in confirmation_message, "Checkout failed - Confirmation message not found"
        time.sleep(5)