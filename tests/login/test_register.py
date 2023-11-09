from playwright.sync_api import Page, expect


def test_check_that_register_button_is_working(page: Page) -> None:
    page.goto("https://automationteststore.com/index.php?rt=account/login")
    page.get_by_role("button", name=" Continue").click()

    register_header = page.locator("span.maintext")

    expect(register_header).to_have_text("Create Account")


def test_check_that_user_is_successfully_registered(page: Page) -> None:
    page.goto("https://automationteststore.com/index.php?rt=account/create")
    page.locator("#AccountFrm_firstname").click()
    page.locator("#AccountFrm_firstname").fill("Tester")
    page.locator("#AccountFrm_lastname").click()
    page.locator("#AccountFrm_lastname").fill("Tester")
    page.locator("#AccountFrm_email").click()
    page.locator("#AccountFrm_email").fill("test@mail.hr")
    page.locator("#AccountFrm_address_1").click()
    page.locator("#AccountFrm_address_1").fill("test address 123")
    page.locator("#AccountFrm_city").click()
    page.locator("#AccountFrm_city").fill("test")
    page.locator("#AccountFrm_zone_id").select_option("3513")
    page.locator("#AccountFrm_postcode").click()
    page.locator("#AccountFrm_postcode").fill("123456")
    page.locator("#AccountFrm_loginname").click()
    page.locator("#AccountFrm_loginname").fill("testertester12")
    page.locator("#AccountFrm_password").click()
    page.locator("#AccountFrm_password").fill("12345")
    page.locator("#AccountFrm_confirm").click()
    page.locator("#AccountFrm_confirm").fill("12345")
    page.get_by_label("I have read and agree to the Privacy Policy").check()
    page.get_by_role("button", name=" Continue").click()

    end_registration_header = page.locator("span.maintext")

    expect(end_registration_header).to_have_text("Your Account Has Been Created!")


def test_check_that_registration_mandatory_fields_must_be_imputed(page: Page) -> None:
    page.goto("https://automationteststore.com/index.php?rt=account/create")
    page.get_by_label("I have read and agree to the Privacy Policy").check()
    page.get_by_role("button", name=" Continue").click()

    end_registration_header = page.locator("class.alert alert-error alert-danger")

    expect(end_registration_header)


def test_check_that_registration_privacy_policy_must_be_accepted(page: Page) -> None:
    page.goto("https://automationteststore.com/index.php?rt=account/create")
    page.get_by_role("button", name=" Continue").click()
    page.locator("#AccountFrm_firstname").click()
    page.locator("#AccountFrm_firstname").fill("Tester")
    page.locator("#AccountFrm_lastname").click()
    page.locator("#AccountFrm_lastname").fill("Tester")
    page.locator("#AccountFrm_email").click()
    page.locator("#AccountFrm_email").fill("test@mail.hr")
    page.locator("#AccountFrm_address_1").click()
    page.locator("#AccountFrm_address_1").fill("test address 123")
    page.locator("#AccountFrm_city").click()
    page.locator("#AccountFrm_city").fill("test")
    page.locator("#AccountFrm_zone_id").select_option("3513")
    page.locator("#AccountFrm_postcode").click()
    page.locator("#AccountFrm_postcode").fill("123456")
    page.locator("#AccountFrm_loginname").click()
    page.locator("#AccountFrm_loginname").fill("testertester12")
    page.locator("#AccountFrm_password").click()
    page.locator("#AccountFrm_password").fill("12345")
    page.locator("#AccountFrm_confirm").click()
    page.locator("#AccountFrm_confirm").fill("12345")

    end_registration_header = page.locator("class.alert alert-error alert-danger")

    expect(end_registration_header)
