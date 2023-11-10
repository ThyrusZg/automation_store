from playwright.sync_api import expect
from automation_store.src.pages.LoginPage import LoginPage
from automation_store.tests.test_data.test_data import TestData


def test_valid_login(login_page_generator):
    login_page = LoginPage(login_page_generator)
    credentials = TestData.valid_login_data()
    login_page.do_login(credentials)
    account_header = login_page.page.locator(TestData.span_maintext())

    expect(account_header).to_be_visible()
    expect(account_header).to_have_text(TestData.my_account_text())


def test_invalid_login(login_page_generator):
    login_page = LoginPage(login_page_generator)
    credentials = TestData.invalid_login_data()
    login_page.do_login(credentials)

    expect(login_page.error_message).to_be_visible()
