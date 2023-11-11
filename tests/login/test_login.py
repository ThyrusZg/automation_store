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


def test_invalid_login_both_credentials(login_page_generator):
    login_page = LoginPage(login_page_generator)
    credentials = TestData.invalid_login_data()
    login_page.do_login(credentials)

    expect(login_page.error_message).to_be_visible()


def test_empty_data_login_attempt(login_page_generator):
    login_page = LoginPage(login_page_generator)
    login_page.click_login_button()

    expect(login_page.error_message).to_be_visible()


def test_empty_username_login_attempt(login_page_generator):
    login_page = LoginPage(login_page_generator)
    login_page.enter_password(TestData.valid_password())
    login_page.click_login_button()

    expect(login_page.error_message).to_be_visible()


def test_empty_password_login_attempt(login_page_generator):
    login_page = LoginPage(login_page_generator)
    login_page.enter_username(TestData.valid_username())
    login_page.click_login_button()

    expect(login_page.error_message).to_be_visible()


def test_invalid_username_login_attempt(login_page_generator):
    login_page = LoginPage(login_page_generator)
    login_page.enter_username(TestData.invalid_username())
    login_page.enter_password(TestData.valid_password())
    login_page.click_login_button()

    expect(login_page.error_message).to_be_visible()


def test_invalid_password_login_attempt(login_page_generator):
    login_page = LoginPage(login_page_generator)
    login_page.enter_username(TestData.valid_username())
    login_page.enter_password(TestData.invalid_password())
    login_page.click_login_button()

    expect(login_page.error_message).to_be_visible()
