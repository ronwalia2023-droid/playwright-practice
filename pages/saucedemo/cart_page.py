class CartPage:
    def __init__(self,page):
        self.page= page
        self.page_title = "[data-test='title']"
        self.product_names = "[data-test='inventory-item-name']"
        self.continue_button = "[data-test='continue-shopping']"
        self.checkout_button = "[data-test='checkout']"
        
    def get_page_title(self):
        return self.page.locator(self.page_title).inner_text()

    def get_product_names(self):
        return self.page.locator(self.product_names).all_inner_texts()

    def remove_product(self, product_slug):
        self.page.locator(f"[data-test='remove-{product_slug}']").click()

    def continue_shopping(self):
        self.page.locator(self.continue_button).click()

    def click_checkout(self):
        self.page.locator(self.checkout_button).click()



    

