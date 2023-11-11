from playwright.sync_api import expect
from automation_store.tests.test_data.test_data import TestData
from automation_store.src.pages.LandingPage import LandingPage


def test_navigate_to_login_page(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.click_login_button()

    login_heading = landing_page.page.locator(TestData.span_maintext())

    expect(login_heading).to_be_visible()
    expect(login_heading).to_have_text(TestData.account_login_text())


def test_check_that_register_button_is_working(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.click_login_button()
    landing_page.click_register_button()

    register_header = landing_page.page.locator(TestData.span_maintext())

    expect(register_header).to_be_visible()
    expect(register_header).to_have_text(TestData.create_account_text())


def test_empty_search(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.click_on_search_button()

    search_header = landing_page.page.locator(TestData.span_maintext())

    expect(search_header).to_be_visible()
    expect(search_header).to_have_text(TestData.search_text())


def test_check_product_in_default_category(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.do_search_in_all_category(TestData.total_moisture_facial_cream())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.total_moisture_facial_cream())


def test_check_product_in_apparel_and_accessories_category(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.do_search_in_apparel_and_accessories_category(TestData.polo_text())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.jersey_cotton_striped_polo_shirt())


def test_check_product_in_makeup_category(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.do_search_in_makeup_category(TestData.waterproof_protective_undereye_concealer())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.waterproof_protective_undereye_concealer())


def test_check_product_in_skincare_category(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.do_search_in_skincare_category(TestData.cream_precieuse_nut())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.cream_precieuse_nut())


def test_check_product_in_fragrance_category(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.do_search_in_fragrance_category(TestData.gucci_guilty())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.gucci_guilty())


def test_check_product_in_men_category(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.do_search_in_men_category(TestData.shower_text())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.men_plus_care_shower_tool())


def test_check_product_in_hair_care_category(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.do_search_in_hair_care_category(TestData.eau_text())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.eau_parfumee_au_the_vert_shampoo())


def test_check_product_in_books_category(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.do_search_in_books_category(TestData.allegiant_by_veronica_roth())

    product_name = landing_page.page.locator(TestData.span_bgnone())

    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.allegiant_by_veronica_roth())


def test_add_product_to_cart_from_default_category_search(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.do_search_in_all_category(TestData.total_moisture_facial_cream())
    landing_page.add_to_chart_in_detailed_view()

    chart_name = landing_page.page.locator(TestData.span_maintext())
    product_name = landing_page.page.get_by_role(TestData.link_text(), name=TestData.total_moisture_facial_cream())

    expect(chart_name).to_be_visible()
    expect(chart_name).to_have_text(TestData.shopping_cart())
    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.total_moisture_facial_cream())


def test_add_product_to_cart_from_makeup_category(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.do_search_in_makeup_category(TestData.waterproof_protective_undereye_concealer())
    landing_page.add_to_chart_in_detailed_view()

    chart_name = landing_page.page.locator(TestData.span_maintext())
    product_name = landing_page.page.get_by_role(TestData.link_text(), name=TestData.waterproof_protective_undereye_concealer())

    expect(chart_name).to_be_visible()
    expect(chart_name).to_have_text(TestData.shopping_cart())
    expect(product_name).to_be_visible()
    expect(product_name).to_have_text(TestData.waterproof_protective_undereye_concealer())


def test_add_product_to_cart_out_stock(landing_page_generator) -> None:
    landing_page = LandingPage(landing_page_generator)
    landing_page.do_search_in_apparel_and_accessories_category(TestData.polo_text())

    out_of_stock_product = landing_page.page.locator(TestData.span_nostock())

    expect(out_of_stock_product).to_be_visible()
    expect(out_of_stock_product).to_have_text(TestData.out_of_stock_text())
