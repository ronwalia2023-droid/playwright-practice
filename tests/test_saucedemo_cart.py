import pytest



@pytest.mark.smoke
def test_cart_page_loads(cart_page):
    assert cart_page.get_page_title() == "Your Cart"
    assert len(cart_page.get_product_names()) == 1


@pytest.mark.regression
def test_remove_item_from_cart(cart_page):
    assert len(cart_page.get_product_names()) ==1
    cart_page.remove_product("sauce-labs-backpack")
    assert len(cart_page.get_product_names()) == 0 

@pytest.mark.regression
def test_continue_shopping(cart_page):
    cart_page.continue_shopping()
    assert "inventory" in cart_page.page.url
