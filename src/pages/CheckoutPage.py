class CheckoutPage:

    def __init__(self, page):
        self.page = page
        self._edit_shipping = page.locator('//*[@id="maincontainer"]/div/div[1]/div/div[2]/table[1]/tbody/tr/td[4]/a')
        self._edit_payment = page.locator('//*[@id="maincontainer"]/div/div[1]/div/div[2]/table[2]/tbody/tr/td[4]/a[1]')
        self._edit_coupon = page.locator('//*[@id="maincontainer"]/div/div[1]/div/div[2]/table[2]/tbody/tr/td[4]/a[2]')
        self._edit_cart = page.locator('//*[@id="maincontainer"]/div/div[1]/div/div[2]/h4[3]/a')
        self._confirm_order = page.locator('//*[@id="checkout_btn"]')
        self._change_address_button = page.locator('//*[@id="shipping"]/div[1]/table/tbody/tr/td[2]/div/div/a')
        self._change_payment_address = page.locator('//*[@id="maincontainer"]/div/div[1]/div/div/div[1]/table/tbody/tr/td[2]/div/div/a')
        self._remove_from_cart = page.locator('//*[@id="cart"]/div/div[1]/table/tbody/tr[2]/td[7]/a/i')
        self._invoice_page_button = page.locator('//*[@id="maincontainer"]/div/div/div/div/section/p[3]/a')
        self._continue_button_completed_payment = page.locator('//*[@id="maincontainer"]/div/div/div/div/section/a')

    def enter_edit_shipping(self):
        self._edit_shipping.click()

    def enter_edit_payment(self):
        self._edit_payment.click()

    def enter_edit_coupon(self):
        self._edit_coupon.click()

    def enter_edit_cart(self):
        self._edit_cart.click()

    def confirm_order(self):
        self._confirm_order.click()

    def change_shipping_address(self):
        self._change_address_button.click()

    def change_payment_address(self):
        self._change_payment_address.click()

    def remove_from_cart(self):
        self._remove_from_cart.click()

    def click_on_invoice(self):
        self._invoice_page_button.click()

    def click_on_continue_when_payment_is_completed(self):
        self._continue_button_completed_payment.click()
