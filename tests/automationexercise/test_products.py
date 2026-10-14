import pytest
from pages.automationexercise.products_page import ProductsPage


@pytest.mark.regression
def test_products_page_loads(page):
    product_page = ProductsPage(page)
    product_page.open()
    assert product_page.get_page_title() == "ALL PRODUCTS"
    assert len(product_page.get_product_names() ) > 0


@pytest.mark.regression
def test_add_to_cart(page):
    product_page = ProductsPage(page)
    product_page.open()
    product_page.add_product_to_cart(4)
    assert product_page.is_added_modal_visible()
    
