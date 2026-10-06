import pytest
from pages.automationexercise.login_page import LoginPage


@pytest.mark.smoke
def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("rtest2026@mailinator.com","wrongpassword")
    assert "Your email or password is incorrect!" in login_page.get_error_message()
