class CheckoutPage:

    def __init__(self, page):
        self.page = page
        self._edit_shipping = page.locator('//*[@id="maincontainer"]/div/div[1]/div/div[2]/table[1]/tbody/tr/td[4]/a')
        self._edit_payment = page.locator('//*[@id="maincontainer"]/div/div[1]/div/div[2]/table[2]/tbody/tr/td[4]/a[1]')
        self._edit_coupon = page.locator('//*[@id="maincontainer"]/div/div[1]/div/div[2]/table[2]/tbody/tr/td[4]/a[2]')
        self._edit_cart = page.locator('//*[@id="maincontainer"]/div/div[1]/div/div[2]/h4[3]/a')
        self._confirm_order = page.locator('//*[@id="checkout_btn"]')

