from playwright.sync_api import expect
from automation_store.src.pages.RegistrationPage import RegistrationPage
from automation_store.tests.test_data.test_data import TestData
from automation_store.src.logger.logger_setup import logger


def test_check_that_user_is_successfully_registered(registration_page_generator) -> None:
    """
    Purpose of this test is to check that user can be successfully registered
    :param registration_page_generator: conftest generated registration page
    :return: None
    """
    logger.info("*** STARTING TEST VALID REGISTRATION TEST ***")
    register_page = RegistrationPage(registration_page_generator)
    credentials = TestData.valid_register_data()

    logger.info("Populating mandatory data in registration fields")
    register_page.do_register_user(credentials)

    account_header = register_page.page.locator(TestData.span_maintext())

    logger.info("Checking data")
    expect(account_header).to_be_visible()
    expect(account_header).to_have_text(TestData.account_created_text())


def test_check_that_registration_mandatory_fields_must_be_imputed(registration_page_generator) -> None:
    """
        Purpose of this test is to check that all mandatory fields must be input in order to register new user
        :param registration_page_generator: conftest generated registration page
        :return: None
        """
    logger.info("*** STARTING TEST MISSING MANDATORY FIELDS ***")
    register_page = RegistrationPage(registration_page_generator)

    logger.info("Accept policy and click on register button, mandatory fields not populated")
    register_page.accept_policy_checkbox_check()
    register_page.click_registration_button()

    logger.info("Checking data")
    expect(register_page.error_message).to_be_visible()


def test_check_that_registration_privacy_policy_must_be_accepted(registration_page_generator) -> None:
    """
        Purpose of this test is to check that privacy policy must be accepted in order to register.
        :param registration_page_generator: conftest generated registration page
        :return: None
        """
    logger.info("*** STARTING TEST POLICY NOT ACCEPTED ***")
    register_page = RegistrationPage(registration_page_generator)
    data = TestData.string_test()

    logger.info("Input data in some mandatory fields and click on register")
    register_page.enter_first_name(data)
    register_page.enter_last_name(data)
    register_page.enter_email(data)
    register_page.enter_zip_code(data)
    register_page.click_registration_button()

    logger.info("Checking data")
    expect(register_page.error_message).to_be_visible()
