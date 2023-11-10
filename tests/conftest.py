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
