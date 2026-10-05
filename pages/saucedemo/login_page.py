class SauceLoginPage:
    def __init__(self,page):
        self.page = page
        self.url = "https://www.saucedemo.com/"
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"


    def open(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.page.locator(self.username_input).fill(username)
        self.page.locator(self.password_input).fill(password)
        self.page.locator(self.login_button).click()

    def get_error_message(self):
        return self.page.locator(self.error_message).inner_text()
    