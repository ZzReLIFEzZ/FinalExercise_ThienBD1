from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class IventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Call the constructor of BasePage
        self.inventory_items = (By.CLASS_NAME, "inventory_item")  # Assuming inventory items have this class
        self.cart_button = (By.ID, "shopping_cart_container")  # Assuming the cart button has this ID
        self.cart_items_count = (By.CLASS_NAME, "shopping_cart_badge")  # Assuming the cart items count has this class
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_primary")       # Assuming add to cart buttons have this class
        

    def get_inventory_items(self):
        """Returns a list of inventory items."""
        return self.wait_for_elements(self.inventory_items)

    def click_cart_button(self):
        """Clicks the cart button and waits for the cart page to load."""
        self.click(self.cart_button)  # Click vào icon giỏ hàng (ở góc phải)

     # Đợi URL chuyển sang trang giỏ hàng
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/cart")
        )

    # (Tùy chọn) Đợi phần tử đặc trưng trong trang giỏ hàng xuất hiện
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cart_list"))
        )

    def get_addable_item_indexes(self):
        inventory_items = self.get_inventory_items()
        print(f"🔎 Tổng số sản phẩm: {len(inventory_items)}")
        addable_indexes = []
        for idx, item in enumerate(inventory_items):
            try:
                item.find_element(By.CSS_SELECTOR, "button.btn_primary")
                print(f"✅ Sản phẩm {idx} còn nút Add to cart")
                addable_indexes.append(idx)
            except:
                print(f"❌ Sản phẩm {idx} KHÔNG có nút Add to cart (có thể đã được thêm)")
                continue
        print(f"📦 Có {len(addable_indexes)} sản phẩm có thể thêm vào giỏ")
        return addable_indexes

    def add_item_to_cart(self, item_index):
        """Adds an item to the cart by its index in the inventory items list."""
        inventory_items = self.get_inventory_items()

        if 0 <= item_index < len(inventory_items):
            try:
                add_button = inventory_items[item_index].find_element(By.CSS_SELECTOR, "button.btn_primary")
                add_button.click()
            except:
                print(f"⚠️ Item {item_index} không có nút Add to cart (có thể đã được thêm)")
        else:
            raise IndexError("Item index out of range")
        