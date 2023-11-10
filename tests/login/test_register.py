from playwright.sync_api import expect

from automation_store.src.pages.RegistrationPage import RegistrationPage


def test_check_that_user_is_successfully_registered(registration_page_generator) -> None:
    register_page = RegistrationPage(registration_page_generator)
    credentials = {"first_name": "test", "last_name": "test", "email": "tes1212t@mail.com", "full_address": "ilica",
                   "city": "zagreb", "region": "3513", "zip_code": "12345", "login_name": "new_tester_123",
                   "password": "abcd1234"}
    register_page.do_register_user(credentials)

    account_header = register_page.page.locator("span.maintext")

    expect(account_header).to_be_visible()
    expect(account_header).to_have_text("Your Account Has Been Created!")


def test_check_that_registration_mandatory_fields_must_be_imputed(registration_page_generator) -> None:
    register_page = RegistrationPage(registration_page_generator)
    register_page.accept_policy_checkbox_check()
    register_page.click_registration_button()

    expect(register_page.error_message).to_be_visible()


def test_check_that_registration_privacy_policy_must_be_accepted(registration_page_generator) -> None:
    register_page = RegistrationPage(registration_page_generator)
    register_page.enter_first_name("test")
    register_page.enter_last_name("test")
    register_page.enter_email("test@mailer.hr")
    register_page.enter_zip_code("10000")
    register_page.click_registration_button()

    expect(register_page.error_message).to_be_visible()
