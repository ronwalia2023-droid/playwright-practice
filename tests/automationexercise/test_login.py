import pytest
from pages.automationexercise.login_page import LoginPage

@pytest.mark.smoke
def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("rtest2026@mailinator.com","rtest2026")
    assert page.locator("a[href='/logout']").is_visible()

