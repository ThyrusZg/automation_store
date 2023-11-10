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

    def click_login_button(self):
        self._login_button.click()

    def click_register_button(self):
        self._register_button.click()
