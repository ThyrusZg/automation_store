class LandingPage:
    def __init__(self, page):
        self.page = page
        self._login_button = page.locator('//*[@id="customer_menu_top"]/li/a')
        self._register_button = page.locator('//*[@id="accountFrm"]/fieldset/button')
        self._cart_button = page.locator('//*[@id="main_menu_top"]/li[3]/a/span')
        self._checkout_button = page.locator('//*[@id="main_menu_top"]/li[4]/a/span')
        self._apparel_and_accessories_button = page.locator('//*[@id="categorymenu"]/nav/ul/li[2]/a')
        self._makeup_button = page.locator('//*[@id="categorymenu"]/nav/ul/li[3]/a')
        self._skincare_button = page.locator('//*[@id="categorymenu"]/nav/ul/li[4]/a')
        self._fragrance_button = page.locator('//*[@id="categorymenu"]/nav/ul/li[5]/a')
        self._men_button = page.locator('//*[@id="categorymenu"]/nav/ul/li[6]/a')
        self._hair_care_button = page.locator('//*[@id="categorymenu"]/nav/ul/li[7]/a')
        self._books_button = page.locator('/html/body/div/div[1]/div[1]/section/nav/ul/li[8]/a')
        self._search_input_field = page.get_by_placeholder("Search Keywords")
        self._search_category_all = page.locator("#category_0")
        self._search_category_apparel_and_accessories = page.locator("#category_68")
        self._search_category_makeup = page.locator("#category_36")
        self._search_category_skincare = page.locator("#category_43")
        self._search_category_fragrance = page.locator("#category_49")
        self._search_category_men = page.locator("#category_58")
        self._search_category_haircare = page.locator("#category_52")
        self._search_category_books = page.locator("#category_65")
        self._search_button = page.get_by_title("Go").locator("i")
        self._add_to_cart_specific_product = page.get_by_role("link", name=" Add to Cart")

    def click_login_button(self):
        self._login_button.click()

    def click_register_button(self):
        self._register_button.click()

    def do_search_in_all_category(self, product_name):
        self._search_input_field.click()
        self._search_category_all.click()
        self._search_input_field.fill(product_name)
        self._search_button.click()

    def do_search_in_apparel_and_accessories_category(self, product_name):
        self._search_input_field.click()
        self._search_category_apparel_and_accessories.click()
        self._search_input_field.fill(product_name)
        self._search_button.click()

    def do_search_in_makeup_category(self, product_name):
        self._search_input_field.click()
        self._search_category_makeup.click()
        self._search_input_field.fill(product_name)
        self._search_button.click()

    def do_search_in_skincare_category(self, product_name):
        self._search_input_field.click()
        self._search_category_skincare.click()
        self._search_input_field.fill(product_name)
        self._search_button.click()

    def do_search_in_fragrance_category(self, product_name):
        self._search_input_field.click()
        self._search_category_fragrance.click()
        self._search_input_field.fill(product_name)
        self._search_button.click()

    def do_search_in_men_category(self, product_name):
        self._search_input_field.click()
        self._search_category_men.click()
        self._search_input_field.fill(product_name)
        self._search_button.click()

    def do_search_in_hair_care_category(self, product_name):
        self._search_input_field.click()
        self._search_category_haircare.click()
        self._search_input_field.fill(product_name)
        self._search_button.click()

    def do_search_in_books_category(self, product_name):
        self._search_input_field.click()
        self._search_category_books.click()
        self._search_input_field.fill(product_name)
        self._search_button.click()

    def add_to_chart_in_detailed_view(self):
        self._add_to_cart_specific_product.click()
