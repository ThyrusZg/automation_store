import pytest


@pytest.fixture(scope="function")
def login_page_generator(page) -> None:
    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("https://automationteststore.com/index.php?rt=account/login")
    yield page


@pytest.fixture(scope="function")
def landing_page_generator(page) -> None:
    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("https://automationteststore.com/")
    yield page


@pytest.fixture(scope="function")
def registration_page_generator(page) -> None:
    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("https://automationteststore.com/index.php?rt=account/create")
    yield page


@pytest.fixture(scope="function")
def checkout_page_generator(page) -> None:
    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("https://automationteststore.com/index.php?rt=account/login")
    page.locator("#loginFrm_loginname").fill("test_automation_user")
    page.locator("#loginFrm_password").fill("1234")
    page.get_by_role("button", name=" Login").click()
    page.goto("https://automationteststore.com")
    page.locator('//*[@id="block_frame_featured_1769"]/div/div[1]/div[2]/div[3]/a').click()
    page.goto("https://automationteststore.com/index.php?rt=checkout/confirm")
    yield page
