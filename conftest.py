import pytest
from pages.saucedemo.login_page import SauceLoginPage
from pages.saucedemo.inventory_page import InventoryPage as SInventoryPage
from pages.saucedemo.cart_page import CartPage as SCartPage
from pages.automationexercise.products_page import ProductsPage
from pages.automationexercise.cart_page import CartPage as ACartPage


# ----------------------------------------------------------------------------
# Sauce Demo fixtures
# ----------------------------------------------------------------------------

@pytest.fixture
def logged_in_page(page):
    login_page = SauceLoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return page


@pytest.fixture
def inventory_page(logged_in_page):
    return SInventoryPage(logged_in_page)


@pytest.fixture
def cart_page(inventory_page):
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    assert inventory_page.get_cart_count() == 1
    inventory_page.go_to_cart()
    inventory_page.page.wait_for_url("**/cart.html", timeout=10000)
    inventory_page.page.wait_for_selector("[data-test='title']:has-text('Your Cart')", timeout=10000)
    return SCartPage(inventory_page.page)


# ----------------------------------------------------------------------------
# automationexercise fixtures
# ----------------------------------------------------------------------------

@pytest.fixture
def ae_cart_page(page):
    products_page= ProductsPage(page)
    products_page.open()
    products_page.add_product_to_cart(1)
    products_page.view_cart_page()
    return ACartPage(page)

