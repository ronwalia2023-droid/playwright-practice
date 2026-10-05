class CheckoutStepTwoPage:
    def __init__(self,page):
        self.page= page
        self.product_names = "[data-test='inventory-item-name']"
        self.total_label = "[data-test='total-label']"
        self.finish_button = "[data-test='finish']"
        self.cancel_button = "[data-test='cancel']"

    def get_product_names(self):
        return self.page.locator(self.product_names).all_inner_texts()

    def get_total_label(self):
        return self.page.locator(self.total_label).inner_text() 
   
    def finish_purchase(self):
        self.page.locator(self.finish_button).click()

    def cancel_purchase(self):
        self.page.locator(self.cancel_button).click()
