class CartPage: 
    def __init__(self,page):
        self.page = page 
        self.url = "https://automationexercise.com/view_cart" 
        self.page_title = "li.active"
        self.product_rows = "tbody tr"
        self.product_names = ".cart_description h4 a" 
        

    def open(self):
        self.page.goto(self.url)


    def get_page_title(self):
        return self.page.locator(self.page_title).inner_text()    


    def get_cart_item_count(self):
        return self.page.locator(self.product_rows).count()


    def remove_item(self,product_id):
        self.page.locator(f"a.cart_quantity_delete[data-product-id='{product_id}']").click()
        self.page.wait_for_selector("#product-1", state="detached")
    