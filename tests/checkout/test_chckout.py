from playwright.sync_api import expect
from automation_store.tests.test_data.test_data import TestData
from automation_store.src.pages.CheckoutPage import CheckoutPage
from automation_store.src.logger.logger_setup import logger


def test_check_that_checkout_page_is_visible(checkout_page_generator) -> None:
    """
    Purpose of this test is to check that checkout page is visible
    :param checkout_page_generator: conftest generated checkout page with logged-in user and item added to cart
    :return:
    """
    logger.info("*** STARTING TEST CHECK THAT CHECKOUT PAGE IS VISIBLE ***")
    checkout_page = CheckoutPage(checkout_page_generator)

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    logger.info("Checking data")
    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.checkout_confirmation_text())


def test_enter_edit_shipping(checkout_page_generator) -> None:
    """
    Purpose of this test is to check that edit shipping button will open shipping panel
    :param checkout_page_generator: conftest generated checkout page with logged-in user and item added to cart
    :return:
    """
    logger.info("*** STARTING TEST CHECK THAT EDIT SHIPPING BUTTON IS WORKING ***")
    checkout_page = CheckoutPage(checkout_page_generator)
    logger.info("Clicking on edit shipping button")
    checkout_page.enter_edit_shipping()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    logger.info("Checking data")
    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.delivery_information_text())


def test_enter_change_shipping_address(checkout_page_generator) -> None:
    """
    Purpose of this test is to check that shipping address edit panel can be accessed by pressing on
    edit shipping button -> shipping address button
    :param checkout_page_generator: conftest generated checkout page with logged-in user and item added to cart
    :return:
    """
    logger.info("*** STARTING TEST CHECK THAT SHIPPING DATA EDIT PANEL IS OPENING ***")
    checkout_page = CheckoutPage(checkout_page_generator)
    logger.info("Click on edit shipping button")
    checkout_page.enter_edit_shipping()
    logger.info("Click on change shipping address button")
    checkout_page.change_shipping_address()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    logger.info("Checking data")
    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.shipping_address_text())


def test_enter_edit_payment(checkout_page_generator) -> None:
    """
    Purpose of this test is to check that payment panel can be accessed by pressing on edit payment button
    :param checkout_page_generator: conftest generated checkout page with logged-in user and item added to cart
    :return:
    """
    logger.info("*** STARTING TEST CHECK THAT EDIT PAYMENT BUTTON IS WORKING ***")
    checkout_page = CheckoutPage(checkout_page_generator)
    logger.info("Click on edit payment button")
    checkout_page.enter_edit_payment()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    logger.info("Checking data")
    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.payment_information_text())


def test_enter_edit_coupon(checkout_page_generator) -> None:
    """
    Purpose of this test is to check that coupon panel can be accessed by pressing on edit coupon button
    :param checkout_page_generator: conftest generated checkout page with logged-in user and item added to cart
    :return:
    """
    logger.info("*** STARTING TEST CHECK THAT EDIT COUPON BUTTON IS WORKING ***")
    checkout_page = CheckoutPage(checkout_page_generator)
    logger.info("Click on edit coupon button")
    checkout_page.enter_edit_coupon()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    logger.info("Checking data")
    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.payment_information_text())


def test_enter_change_coupon(checkout_page_generator) -> None:
    """
    Purpose of this test is to check that payment address editor can be accessed by pressing on
    edit coupon button -> payment address button
    :param checkout_page_generator: conftest generated checkout page with logged-in user and item added to cart
    :return:
    """
    logger.info("*** STARTING TEST CHECK THAT PAYMENT DATA EDIT PANEL IS OPENING ***")
    checkout_page = CheckoutPage(checkout_page_generator)
    logger.info("Click on edit coupon button")
    checkout_page.enter_edit_coupon()
    logger.info("Click on change payment address button")
    checkout_page.change_payment_address()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    logger.info("Checking data")
    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.payment_address_text())


def test_enter_edit_cart(checkout_page_generator) -> None:
    """
    Purpose of this test is to check that edit cart panel can be accessed by pressing on edit cart button
    :param checkout_page_generator: conftest generated checkout page with logged-in user and item added to cart
    :return:
    """
    logger.info("*** STARTING TEST CHECK THAT EDIT CART BUTTON IS WORKING ***")
    checkout_page = CheckoutPage(checkout_page_generator)
    logger.info("Click on edit cart button")
    checkout_page.enter_edit_cart()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    logger.info("Checking data")
    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.shopping_cart())


def test_remove_item_from_shopping_cart(checkout_page_generator) -> None:
    """
    Purpose of this test is to check that item can be successfully removed from cart by pressing on remove from cart
    button that is located in edit cart panel
    :param checkout_page_generator: conftest generated checkout page with logged-in user and item added to cart
    :return:
    """
    logger.info("*** STARTING TEST REMOVE ITEM FROM SHOPPING CART ***")
    checkout_page = CheckoutPage(checkout_page_generator)
    logger.info("Click on edit cart button")
    checkout_page.enter_edit_cart()
    logger.info("Click on remove product button")
    checkout_page.remove_from_cart()

    login_heading = checkout_page.page.locator(TestData.contentpanel_text())

    logger.info("Checking data")
    expect(login_heading).to_be_visible()
    expect(login_heading).to_contain_text(TestData.your_shopping_cart_is_empty_text())


def test_complete_payment(checkout_page_generator) -> None:
    """
    Purpose of this test is to check that order can be successfully confirmed
    :param checkout_page_generator: conftest generated checkout page with logged-in user and item added to cart
    :return:
    """
    logger.info("*** STARTING TEST COMPLETE ORDER ***")
    checkout_page = CheckoutPage(checkout_page_generator)
    logger.info("Click on confirm order button")
    checkout_page.confirm_order()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    logger.info("Checking data")
    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.processed_order_text())


def test_open_payment_invoice(checkout_page_generator) -> None:
    """
    Purpose of this test is to check that payment invoice can be successfully opened when order is completed by
    pressing on invoice button
    :param checkout_page_generator: conftest generated checkout page with logged-in user and item added to cart
    :return:
    """
    logger.info("*** STARTING TEST OPEN INVOICE PAGE WHEN ORDER IS COMPLETED ***")
    checkout_page = CheckoutPage(checkout_page_generator)
    logger.info("Click on confirm order button")
    checkout_page.confirm_order()
    logger.info("Click on invoice button")
    checkout_page.click_on_invoice()

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    logger.info("Checking data")
    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.invoice_order_text())
