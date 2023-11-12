from playwright.sync_api import expect
from automation_store.tests.test_data.test_data import TestData
from automation_store.src.pages.LandingPage import LandingPage
from automation_store.src.logger.logger_setup import logger


def test_navigate_to_login_page(landing_page_generator) -> None:
    """
    Purpose of this test is to check that login page can be accessed by pressing on login button
    :param landing_page_generator: conftest generated landing page (home page)
    :return: None
    """
    logger.info("*** STARTING TEST NAVIGATE TO LOGIN PAGE FROM LANDING PAGE ***")
    landing_page = LandingPage(landing_page_generator)
    logger.info("Click on login button")
    landing_page.click_login_button()

    login_heading = landing_page.page.locator(TestData.span_maintext())

    logger.info("Checking data")
    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.account_login_text())


def test_check_that_register_button_is_working(landing_page_generator) -> None:
    """
    Purpose of this test is to check that register page can be accessed by pressing on register button in login panel
    :param landing_page_generator: conftest generated landing page (home page)
    :return: None
    """
    logger.info("*** STARTING TEST CHECK THAT REGISTER BUTTON IS WORKING ***")
    landing_page = LandingPage(landing_page_generator)
    logger.info("Click on login button")
    landing_page.click_login_button()
    logger.info("Click on register button")
    landing_page.click_register_button()

    register_header = landing_page.page.locator(TestData.span_maintext())

    logger.info("Checking data")
    expect(register_header).to_be_visible()
    expect(register_header).to_have_text(TestData.create_account_text())


def test_empty_search(landing_page_generator) -> None:
    """
    Purpose of this test is to check that emtpy search is allowed by clicking on search button without any data to
    search in search input field
    :param landing_page_generator: conftest generated landing page (home page)
    :return: None
    """
    logger.info("*** STARTING TEST EMPTY SEARCH ***")
    landing_page = LandingPage(landing_page_generator)
    logger.info("Click on search button")
    landing_page.click_on_search_button()

    search_header = landing_page.page.locator(TestData.span_maintext())

    logger.info("Checking data")
    expect(search_header).to_be_visible()
    expect(search_header).to_have_text(TestData.search_text())


def test_check_product_in_default_category(landing_page_generator) -> None:
    """
    Purpose of this test is to check that specific product can be searched in default/all category
    :param landing_page_generator: conftest generated landing page (home page)
    :return: None
    """
    logger.info("*** STARTING TEST SEARCH IN DEFAULT CATEGORY ***")
    landing_page = LandingPage(landing_page_generator)
    logger.info("Search for specific product in all category")
    landing_page.do_search_in_all_category(TestData.total_moisture_facial_cream())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    logger.info("Checking data")
    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.total_moisture_facial_cream())


def test_check_product_in_apparel_and_accessories_category(landing_page_generator) -> None:
    """
    Purpose of this test is to check that specific product can be searched in apparel and accessories category
    :param landing_page_generator: conftest generated landing page (home page)
    :return: None
    """
    logger.info("*** STARTING TEST SEARCH IN APPAREL AND ACCESSORIES CATEGORY***")
    landing_page = LandingPage(landing_page_generator)
    logger.info("Search for specific product in apparel and accessories category")
    landing_page.do_search_in_apparel_and_accessories_category(TestData.polo_text())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    logger.info("Checking data")
    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.jersey_cotton_striped_polo_shirt())


def test_check_product_in_makeup_category(landing_page_generator) -> None:
    """
    Purpose of this test is to check that specific product can be searched in makeup category
    :param landing_page_generator: conftest generated landing page (home page)
    :return: None
    """
    logger.info("*** STARTING TEST SEARCH IN MAKEUP CATEGORY ***")
    landing_page = LandingPage(landing_page_generator)
    logger.info("Search for specific product in makeup category")
    landing_page.do_search_in_makeup_category(TestData.waterproof_protective_undereye_concealer())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    logger.info("Checking data")
    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.waterproof_protective_undereye_concealer())


def test_check_product_in_skincare_category(landing_page_generator) -> None:
    """
    Purpose of this test is to check that specific product can be searched in skincare category
    :param landing_page_generator: conftest generated landing page (home page)
    :return: None
    """
    logger.info("*** STARTING TEST SEARCH IN SKINCARE CATEGORY ***")
    landing_page = LandingPage(landing_page_generator)
    logger.info("Search for specific product in makeup category")
    landing_page.do_search_in_skincare_category(TestData.cream_precieuse_nut())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    logger.info("Checking data")
    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.cream_precieuse_nut())


def test_check_product_in_fragrance_category(landing_page_generator) -> None:
    """
    Purpose of this test is to check that specific product can be searched in fragrance category
    :param landing_page_generator: conftest generated landing page (home page)
    :return: None
    """
    logger.info("*** STARTING TEST SEARCH IN FRAGRANCE CATEGORY ***")
    landing_page = LandingPage(landing_page_generator)
    logger.info("Search for specific product in makeup category")
    landing_page.do_search_in_fragrance_category(TestData.gucci_guilty())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    logger.info("Checking data")
    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.gucci_guilty())


def test_check_product_in_men_category(landing_page_generator) -> None:
    """
    Purpose of this test is to check that specific product can be searched in men category
    :param landing_page_generator: conftest generated landing page (home page)
    :return: None
    """
    logger.info("*** STARTING TEST SEARCH IN MEN CATEGORY ***")
    landing_page = LandingPage(landing_page_generator)
    logger.info("Search for specific product in men category")
    landing_page.do_search_in_men_category(TestData.shower_text())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    logger.info("Checking data")
    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.men_plus_care_shower_tool())


def test_check_product_in_hair_care_category(landing_page_generator) -> None:
    """
    Purpose of this test is to check that specific product can be searched in hair care category
    :param landing_page_generator: conftest generated landing page (home page)
    :return: None
    """
    logger.info("*** STARTING TEST SEARCH IN HAIR CARE CATEGORY ***")
    landing_page = LandingPage(landing_page_generator)
    logger.info("Search for specific product in hair care category")
    landing_page.do_search_in_hair_care_category(TestData.eau_text())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    logger.info("Checking data")
    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.eau_parfumee_au_the_vert_shampoo())


def test_check_product_in_books_category(landing_page_generator) -> None:
    """
    Purpose of this test is to check that specific product can be searched in books category
    :param landing_page_generator: conftest generated landing page (home page)
    :return: None
    """
    logger.info("*** STARTING TEST SEARCH IN BOOKS CATEGORY ***")
    landing_page = LandingPage(landing_page_generator)
    logger.info("Search for specific product in books category")
    landing_page.do_search_in_books_category(TestData.allegiant_by_veronica_roth())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    logger.info("Checking data")
    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.allegiant_by_veronica_roth())


def test_add_product_to_cart_from_default_category_search(landing_page_generator) -> None:
    """
    Purpose of this test is to check that specific product can be searched in default/all category and that product
    which is found can be successfully added to cart
    :param landing_page_generator: conftest generated landing page (home page)
    :return: None
    """
    logger.info("*** STARTING TEST ADD PRODUCT TO CART FROM DEFAULT SEARCH ***")
    landing_page = LandingPage(landing_page_generator)
    logger.info("Search for specific product in all category")
    landing_page.do_search_in_all_category(TestData.total_moisture_facial_cream())
    logger.info("Add product to cart")
    landing_page.add_to_chart_in_detailed_view()

    chart_name = landing_page.page.locator(TestData.span_maintext())
    product_name = landing_page.page.get_by_role(TestData.link_text(), name=TestData.total_moisture_facial_cream())

    logger.info("Checking data")
    expect(chart_name).to_be_visible()
    expect(chart_name).to_have_text(TestData.shopping_cart())
    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.total_moisture_facial_cream())


def test_add_product_to_cart_from_makeup_category(landing_page_generator) -> None:
    """
    Purpose of this test is to check that specific product can be searched in makeup category and that product
    which is found can be successfully added to cart
    :param landing_page_generator: conftest generated landing page (home page)
    :return: None
    """
    logger.info("*** STARTING TEST ADD PRODUCT TO CART FROM MAKEUP CATEGORY ***")
    landing_page = LandingPage(landing_page_generator)
    logger.info("Search for specific product in makeup category")
    landing_page.do_search_in_makeup_category(TestData.waterproof_protective_undereye_concealer())
    logger.info("Add product to cart")
    landing_page.add_to_chart_in_detailed_view()

    chart_name = landing_page.page.locator(TestData.span_maintext())
    product_name = landing_page.page.get_by_role(TestData.link_text(), name=TestData.waterproof_protective_undereye_concealer())

    logger.info("Checking data")
    expect(chart_name).to_be_visible()
    expect(chart_name).to_have_text(TestData.shopping_cart())
    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.waterproof_protective_undereye_concealer())


def test_add_product_to_cart_out_stock(landing_page_generator) -> None:
    """
    Purpose of this test is to check that specific product can be searched in apparel and accessories category and
    found product that is out of stock will have out of stock label.
    :param landing_page_generator: conftest generated landing page (home page)
    :return: None
    """
    logger.info("*** STARTING TEST CHECK THAT PRODUCT IS OUT OF STOCK ***")
    landing_page = LandingPage(landing_page_generator)
    logger.info("Search for specific product in apparel and accessories category")
    landing_page.do_search_in_apparel_and_accessories_category(TestData.polo_text())

    out_of_stock_product = landing_page.page.locator(TestData.span_nostock())

    logger.info("Check that product is out of stock")
    expect(out_of_stock_product).to_be_visible()
    expect(out_of_stock_product).to_have_text(TestData.out_of_stock_text())
