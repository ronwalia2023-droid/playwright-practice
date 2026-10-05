class InventoryPage:
    def __init__(self,page):
        self.page = page
        self.page_title = "[data-test='title']"
        self.product_names = "[data-test='inventory-item-name']"
        self.cart_link = "[data-test='shopping-cart-link']"
        self.cart_badge = "[data-test='shopping-cart-badge']"

    def get_page_title(self):
        return self.page.locator(self.page_title).inner_text()

    def get_product_names(self):
        return self.page.locator(self.product_names).all_inner_texts()

    def get_product_count(self):
        return self.page.locator(self.product_names).count()

    def get_cart_count(self):
        badge = self.page.locator(self.cart_badge)
        if badge.count() == 0:
           return 0
        return int(badge.inner_text())

    def add_product_to_cart(self, product_slug):
        self.page.locator(f"[data-test='add-to-cart-{product_slug}']").click()
    
    def go_to_cart(self):
        self.page.locator(self.cart_link).click()

    
    


