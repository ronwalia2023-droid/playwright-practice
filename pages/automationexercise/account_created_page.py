class AccountCreatedPage:
    def __init__(self,page):
        self.page= page 
        self.url= "https://automationexercise.com/account_created"
        self.account_created = "[data-qa='account-created']"
        self.continue_button= "[data-qa='continue-button']"

    def is_account_created(self):
        return self.page.locator(self.account_created).is_visible()

    def continue_to_home(self):
        self.page.locator(self.continue_button).click()
        self.page.wait_for_url("https://automationexercise.com/", timeout=10000)
