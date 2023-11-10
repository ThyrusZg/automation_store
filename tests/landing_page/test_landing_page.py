from playwright.sync_api import expect

from automation_store.src.pages.LandingPage import LandingPage


def test_navigate_to_login_page(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.click_login_button()

    login_heading = landing_page.page.locator("span.maintext")

    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text("Account Login")


def test_check_that_register_button_is_working(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.click_login_button()
    landing_page.click_register_button()

    register_header = landing_page.page.locator("span.maintext")

    expect(register_header).to_be_visible()
    expect(register_header).to_have_text("Create Account")