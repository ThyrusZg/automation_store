from playwright.sync_api import expect
from automation_store.tests.test_data.test_data import TestData
from automation_store.src.pages.CheckoutPage import CheckoutPage


def test_check_that_checkout_page_is_visible(checkout_page_generator) -> None:
    checkout_page = CheckoutPage(checkout_page_generator)

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.checkout_confirmation_text())


def test_enter_edit_shipping(checkout_page_generator) -> None:
    checkout_page = CheckoutPage(checkout_page_generator)
    checkout_page.enter_edit_shipping()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.delivery_information_text())


def test_enter_change_shipping_address(checkout_page_generator) -> None:
    checkout_page = CheckoutPage(checkout_page_generator)
    checkout_page.enter_edit_shipping()
    checkout_page.change_shipping_address()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.shipping_address_text())


def test_enter_edit_payment(checkout_page_generator) -> None:
    checkout_page = CheckoutPage(checkout_page_generator)
    checkout_page.enter_edit_payment()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.payment_information_text())


def test_enter_edit_coupon(checkout_page_generator) -> None:
    checkout_page = CheckoutPage(checkout_page_generator)
    checkout_page.enter_edit_coupon()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.payment_information_text())


def test_enter_change_coupon(checkout_page_generator) -> None:
    checkout_page = CheckoutPage(checkout_page_generator)
    checkout_page.enter_edit_coupon()
    checkout_page.change_payment_address()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.payment_address_text())


def test_enter_edit_cart(checkout_page_generator) -> None:
    checkout_page = CheckoutPage(checkout_page_generator)
    checkout_page.enter_edit_cart()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.shopping_cart())


def test_remove_item_from_shopping_cart(checkout_page_generator) -> None:
    checkout_page = CheckoutPage(checkout_page_generator)
    checkout_page.enter_edit_cart()
    checkout_page.remove_from_cart()

    login_heading = checkout_page.page.locator(TestData.contentpanel_text())

    expect(login_heading).to_be_visible()
    expect(login_heading).to_contain_text(TestData.your_shopping_cart_is_empty_text())


def test_complete_payment(checkout_page_generator) -> None:
    checkout_page = CheckoutPage(checkout_page_generator)
    checkout_page.confirm_order()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.processed_order_text())


def test_open_payment_invoice(checkout_page_generator) -> None:
    checkout_page = CheckoutPage(checkout_page_generator)
    checkout_page.confirm_order()
    checkout_page.click_on_invoice()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.invoice_order_text())
