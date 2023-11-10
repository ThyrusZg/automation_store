from playwright.sync_api import expect

from automation_store.src.pages.LoginPage import LoginPage


def test_valid_login(login_page_generator):
    login_page = LoginPage(login_page_generator)
    credentials = {"username": "test_automation_user", "password": "1234"}
    login_page.do_login(credentials)
    account_header = login_page.page.locator("span.maintext")

    expect(account_header).to_be_visible()
    expect(account_header).to_have_text("My Account")


def test_invalid_login(login_page_generator):
    login_page = LoginPage(login_page_generator)
    credentials = {"username": "none", "password": "none"}
    login_page.do_login(credentials)

    expect(login_page.error_message).to_be_visible()
