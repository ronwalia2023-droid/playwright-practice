class ProductsPage:
    def __init__(self,page):
        self.page= page
        self.url = "https://automationexercise.com/products"
        self.page_title= "h2.title.text-center"
        self.product_names = ".productinfo p"
        self.modal_title= "h4.modal-title"
        self.view_cart= "a[href='/view_cart']"  
        self.continue_shopping_button = "button.close-modal"


    def open(self):
        self.page.goto(self.url)

    def get_page_title(self):
        return self.page.locator(self.page_title).inner_text()

    def get_product_names(self):
        return self.page.locator(self.product_names).all_inner_texts()

    def add_product_to_cart(self,product_id):
        self.page.locator(f"a[data-product-id='{product_id}']").first.click()
        self.page.wait_for_selector(self.modal_title, timeout=10000)

    def is_added_modal_visible(self):
        return self.page.locator(self.modal_title).is_visible()    

    def view_cart_page(self):
        self.page.locator(self.view_cart).click()
        self.page.wait_for_url("**/view_cart", timeout=10000)

    def continue_shopping(self):
        self.page.locator(self.continue_shopping_button).click()
        