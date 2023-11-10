from playwright.sync_api import expect
from automation_store.tests.test_data.test_data import TestData
from automation_store.src.pages.LandingPage import LandingPage


def xtest_navigate_to_login_page(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.click_login_button()

    login_heading = landing_page.page.locator(TestData.span_maintext())

    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.account_login_text())


def xtest_check_that_register_button_is_working(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.click_login_button()
    landing_page.click_register_button()

    register_header = landing_page.page.locator(TestData.span_maintext())

    expect(register_header).to_be_visible()
    expect(register_header).to_have_text(TestData.create_account_text())


def test_check_product_in_makeup_category(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.do_search_in_makeup_category(TestData.waterproof_protective_undereye_concealer())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.waterproof_protective_undereye_concealer())


def test_check_product_in_all_category(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.do_search_in_makeup_category(TestData.waterproof_protective_undereye_concealer())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.waterproof_protective_undereye_concealer())
