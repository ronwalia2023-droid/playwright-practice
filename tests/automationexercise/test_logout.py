import pytest
from pages.automationexercise.login_page import LoginPage



@pytest.mark.smoke
def test_logout(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("rtest2026@mailinator.com","rtest2026")
    login_page.logout()
    assert page.locator("a[href='/logout']").is_hidden()

