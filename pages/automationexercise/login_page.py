class LoginPage:
    def __init__(self,page):
        self.page= page
        self.url = "https://automationexercise.com/login"
        self.email_input = "[data-qa='login-email']"
        self.password_input = "[data-qa='login-password']"
        self.login_button = "[data-qa='login-button']"

    def open(self):
        self.page.goto(self.url)

    def login(self, email, password):
        self.page.locator(self.email_input).fill(email)
        self.page.locator(self.password_input).fill(password)
        self.page.locator(self.login_button).click()






