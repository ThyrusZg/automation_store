import pytest


@pytest.fixture(scope="function")
def set_up_tear_down(page) -> None:
    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("https://automationteststore.com/index.php?rt=account/login")
