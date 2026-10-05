class SecureAreaPage:
    def __init__(self, page):
        self.page = page
        self.flash_message = "#flash"
        self.logout_button = "a.button.secondary.radius"

    def get_flash_message(self):
        return self.page.locator(self.flash_message).inner_text()

    def logout(self):
        self.page.locator(self.logout_button).click()