from playwright.sync_api import expect
from automation_store.tests.test_data.test_data import TestData
from automation_store.src.pages.CheckoutPage import CheckoutPage


def test_check_that_checkout_page_is_visible(checkout_page_generator) -> None:
    checkout_page = CheckoutPage(checkout_page_generator)

    login_heading = checkout_page.page.locator(TestData.span_maintext())

    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.checkout_confirmation_text())
