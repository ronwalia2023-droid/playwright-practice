import pytest 
from pages.saucedemo.checkout_step_one_page import CheckoutStepOnePage
from pages.saucedemo.checkout_step_two_page import CheckoutStepTwoPage
from pages.saucedemo.checkout_complete_page import CheckoutCompletePage

@pytest.mark.regression
def test_full_checkout_flow(cart_page):
    cart_page.click_checkout()

    step_one= CheckoutStepOnePage(cart_page.page)
    step_one.fill_info("John","Doe", "90210")
    step_one.click_continue()

    step_two= CheckoutStepTwoPage(cart_page.page)
    assert len(step_two.get_product_names()) == 1
    step_two.finish_purchase()

    complete = CheckoutCompletePage(cart_page.page)
    assert complete.get_confirmation_header() == "Thank you for your order!"

