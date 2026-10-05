class CheckoutCompletePage:
    def __init__(self,page):
        self.page= page
        self.confirmation_header = "[data-test='complete-header']"
        self.confirmation_text = "[data-test='complete-text']"
        self.back_home_button = "[data-test='back-to-products']"
                
    def get_confirmation_header(self):
        return self.page.locator(self.confirmation_header).inner_text()

    def get_confirmation_text(self):
        return self.page.locator(self.confirmation_text).inner_text()

    def click_back_home_button(self):
        self.page.locator(self.back_home_button).click()
