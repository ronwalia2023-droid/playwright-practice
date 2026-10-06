class LoginPage:
    def __init__(self,page):
        self.page= page
        self.url = "https://automationexercise.com/login"
        self.email_input = "[data-qa='login-email']"
        self.password_input = "[data-qa='login-password']"
        self.login_button = "[data-qa='login-button']"
        self.logout_link = "a[href='/logout']"
        self.error_message = "p:has-text('Your email or password is incorrect!')"

    def open(self):
        self.page.goto(self.url)

    def login(self, email, password):
        self.page.locator(self.email_input).fill(email)
        self.page.locator(self.password_input).fill(password)
        self.page.locator(self.login_button).click()

    def logout(self):
        self.page.locator(self.logout_link).click()
        self.page.wait_for_url("**/login", timeout=10000)

    def get_error_message(self):
        return self.page.locator(self.error_message).inner_text()
        



