from playwright.sync_api import expect
from automation_store.src.pages.RegistrationPage import RegistrationPage
from automation_store.tests.test_data.test_data import TestData


def test_check_that_user_is_successfully_registered(registration_page_generator) -> None:
    register_page = RegistrationPage(registration_page_generator)
    credentials = TestData.valid_register_data()
    register_page.do_register_user(credentials)

    account_header = register_page.page.locator(TestData.span_maintext())

    expect(account_header).to_be_visible()
    expect(account_header).to_have_text(TestData.account_created_text())


def test_check_that_registration_mandatory_fields_must_be_imputed(registration_page_generator) -> None:
    register_page = RegistrationPage(registration_page_generator)
    register_page.accept_policy_checkbox_check()
    register_page.click_registration_button()

    expect(register_page.error_message).to_be_visible()


def test_check_that_registration_privacy_policy_must_be_accepted(registration_page_generator) -> None:
    register_page = RegistrationPage(registration_page_generator)
    data = TestData.string_test()
    register_page.enter_first_name(data)
    register_page.enter_last_name(data)
    register_page.enter_email(data)
    register_page.enter_zip_code(data)
    register_page.click_registration_button()

    expect(register_page.error_message).to_be_visible()
