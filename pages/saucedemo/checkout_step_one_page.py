class CheckoutStepOnePage:
    def __init__(self,page):
        self.page= page
        self.first_name_input = "[data-test='firstName']"
        self.last_name_input = "[data-test='lastName']"
        self.zip_input = "[data-test='postalCode']"
        self.continue_button = "[data-test='continue']"
        self.cancel_button = "[data-test='cancel']"

    def fill_info(self, first_name, last_name, zip_code):
        self.page.locator(self.first_name_input).fill(first_name)
        self.page.locator(self.last_name_input).fill(last_name)
        self.page.locator(self.zip_input).fill(zip_code)

    def click_continue(self):
        self.page.locator(self.continue_button).click()

    def click_cancel(self):
        self.page.locator(self.cancel_button).click()

