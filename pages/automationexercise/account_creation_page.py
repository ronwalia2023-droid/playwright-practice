class AccountCreationPage:
    def __init__(self,page):
        self.page = page
        self.url = "https://automationexercise.com/signup"
        self.password_input = "[data-qa='password']"
        self.first_name_input ="[data-qa='first_name']"
        self.last_name_input = "[data-qa='last_name']" 
        self.address_input= "[data-qa='address']"
        self.country_input= "[data-qa='country']"
        self.state_input="[data-qa='state']"
        self.city_input="[data-qa='city']"
        self.zip_input= "[data-qa='zipcode']"
        self.mobile_input="[data-qa='mobile_number']"
        self.create_account_button= "[data-qa='create-account']"

    def complete_account(self, password, first_name, last_name, address, country, 
                         state, city, zip_code, mobile):
        self.page.locator(self.password_input).fill(password)
        self.page.locator(self.first_name_input).fill(first_name)
        self.page.locator(self.last_name_input).fill(last_name)
        self.page.locator(self.address_input).fill(address)
        self.page.locator(self.country_input).select_option(country)
        self.page.locator(self.state_input).fill(state)
        self.page.locator(self.city_input).fill(city)
        self.page.locator(self.zip_input).fill(zip_code)
        self.page.locator(self.mobile_input).fill(mobile)
        self.page.locator(self.create_account_button).click()
        self.page.wait_for_selector("[data-qa='account-created']", timeout=10000)
