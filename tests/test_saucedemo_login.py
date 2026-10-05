import pytest
from pages.saucedemo.login_page import SauceLoginPage
from data.csv_loader import load_csv


all_users = load_csv("saucedemo_users.csv")
valid_users = [u for u in all_users if u["type"] == "valid"]
invalid_users = [u for u in all_users if u["type"] == "invalid"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case", 
    valid_users, 
    ids=[u["username"] for u in valid_users],)    

def test_valid_login(page, case):
    login_page = SauceLoginPage(page)
    login_page.open()
    login_page.login(case["username"], case["password"])
    assert page.url == case["expected"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    invalid_users,
    ids=[f"{u['username']}-{u['password']}" for u in invalid_users],
)
def test_invalid_login(page, case):
    login_page = SauceLoginPage(page)
    login_page.open()
    login_page.login(case["username"], case["password"])
    assert case["expected"] in login_page.get_error_message()