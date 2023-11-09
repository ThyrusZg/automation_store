from playwright.sync_api import Page, expect


def test_navigate_to_login_page(page: Page) -> None:
    page.goto("https://automationteststore.com/")
    page.get_by_role("link", name="Login or register").click()

    login_header = page.locator("span.maintext")

    expect(login_header).to_have_text("Account Login")


def test_login_with_valid_user(page: Page) -> None:
    page.goto("https://automationteststore.com/index.php?rt=account/login")
    page.locator("#loginFrm_loginname").click()
    page.locator("#loginFrm_loginname").fill("test_automation_user")
    page.locator("#loginFrm_password").click()
    page.locator("#loginFrm_password").fill("1234")
    page.get_by_role("button", name=" Login").click()

    login_header = page.locator("span.maintext")

    expect(login_header).to_have_text("My Account")


def test_invalid_login(page: Page) -> None:
    page.goto("https://automationteststore.com/index.php?rt=account/login")
    page.locator("#loginFrm_loginname").click()
    page.locator("#loginFrm_loginname").fill("tester")
    page.locator("#loginFrm_password").click()
    page.locator("#loginFrm_password").fill("1234")
    page.get_by_role("button", name=" Login").click()

    login_header_error = page.locator("class.alert alert-error alert-danger")

    expect(login_header_error).to_be_visible()