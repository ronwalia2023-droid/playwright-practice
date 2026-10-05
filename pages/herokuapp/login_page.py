class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/login"
        self.username_input = "#username"
        self.password_input = "#password"
        self.submit_button = "button[type='submit']"
        self.flash_message = "#flash"

    def open(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.page.locator(self.username_input).fill(username)
        self.page.locator(self.password_input).fill(password)
        self.page.locator(self.submit_button).click()

    def get_flash_message(self):
        return self.page.locator(self.flash_message).inner_text()