class SignupPage:
    def __init__(self,page):
        self.page= page
        self.url = "https://automationexercise.com/login"
        self.signup_name_input = "[data-qa='signup-name']"
        self.signup_email_input = "[data-qa='signup-email']"
        self.signup_button = "[data-qa='signup-button']"

    def open(self):
        self.page.goto(self.url)

    def submit_signup(self,name,email):
        self.page.locator(self.signup_name_input).fill(name)
        self.page.locator(self.signup_email_input).fill(email)
        self.page.locator(self.signup_button).click()
        self.page.wait_for_selector("[data-qa='password']", timeout=10000)

    