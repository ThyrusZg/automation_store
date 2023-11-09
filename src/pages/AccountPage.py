class AccountPage:

    def __init__(self, page):
        self.page = page
        self._account_header = page.locator("span.maintext")

    @property
    def product_header(self):
        return self.product_header()
