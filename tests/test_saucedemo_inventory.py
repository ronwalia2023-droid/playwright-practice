import pytest
from pages.saucedemo.inventory_page import InventoryPage


@pytest.mark.smoke
def test_inventory_loads(inventory_page):
    assert inventory_page.get_page_title() == "Products"
    assert inventory_page.get_product_count() == 6


@pytest.mark.smoke
def test_add_one_item_to_cart(inventory_page):
    assert inventory_page.get_cart_count() == 0
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    assert inventory_page.get_cart_count() == 1


@pytest.mark.regression
def test_add_two_items_to_cart(inventory_page):
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.add_product_to_cart("sauce-labs-bike-light")
    assert inventory_page.get_cart_count() == 2