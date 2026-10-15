import pytest
from pages.automationexercise.signup_page import SignupPage
from pages.automationexercise.account_creation_page import AccountCreationPage
from pages.automationexercise.account_created_page import AccountCreatedPage
import time

@pytest.mark.regression
def test_full_signup(page):
    sign_up_page = SignupPage(page)
    sign_up_page.open()
    email= f"qatest{int(time.time())}@mailinator.com"
    sign_up_page.submit_signup("Tom", email)
    account_creation_page= AccountCreationPage(page)
    account_creation_page.complete_account( "1234", "Tom", "Smith", "123 abc rd", "Canada", 
                         "Ontario", "milton" , "L4V-9F9", "416-967-1111")
    account_created_page=  AccountCreatedPage(page)
    assert account_created_page.is_account_created()
    account_created_page.continue_to_home()



