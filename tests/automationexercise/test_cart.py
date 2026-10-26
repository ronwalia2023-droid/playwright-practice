import pytest 
from pages.automationexercise.products_page import ProductsPage


@pytest.mark.regression
def test_cart_page_loads(ae_cart_page):
    assert ae_cart_page.get_page_title() =="Shopping Cart"
    assert ae_cart_page.get_cart_item_count() == 1

@pytest.mark.regression
def test_remove_item_from_cart(ae_cart_page):
    ae_cart_page.remove_item(1)
    assert ae_cart_page.get_cart_item_count() == 0 

