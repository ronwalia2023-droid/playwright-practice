import pytest
from pages.herokuapp.login_page import LoginPage
from pages.herokuapp.secure_area_page import SecureAreaPage

@pytest.mark.external
@pytest.mark.parametrize("username, password, expected_message", [
    ("tomsmith",  "SuperSecretPassword!", "You logged into a secure area!"),
    ("tomsmith",  "wrongpass",            "Your password is invalid!"),
    ("wronguser", "SuperSecretPassword!", "Your username is invalid!"),
])
def test_login(login_page, username, password, expected_message):
    login_page.login(username, password)
    assert expected_message in login_page.get_flash_message()


@pytest.mark.regression 
def test_login_then_logout(login_page, page):
    login_page.login("tomsmith", "SuperSecretPassword!")

    secure_page = SecureAreaPage(page)
    assert "You logged into a secure area!" in secure_page.get_flash_message()

    secure_page.logout()
    assert "You logged out of the secure area!" in login_page.get_flash_message()