import pytest 
from pages.herokuapp.login_page import LoginPage
from pages.saucedemo.login_page import SauceLoginPage
from pages.saucedemo.inventory_page import InventoryPage
from pages.saucedemo.cart_page import CartPage



@pytest.fixture
def login_page(page):
    lp= LoginPage(page)
    lp.open()
    return lp

@pytest.fixture
def logged_in_page(page):
    login_page=SauceLoginPage(page)
    login_page.open()
    login_page.login("standard_user","secret_sauce")
    return page 

@pytest.fixture
def inventory_page(logged_in_page):
    return InventoryPage(logged_in_page)

@pytest.fixture
def cart_page(inventory_page):
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    assert inventory_page.get_cart_count() == 1
    inventory_page.go_to_cart()
    inventory_page.page.wait_for_url("**/cart.html")     ← this line?
    return CartPage(inventory_page.page)
