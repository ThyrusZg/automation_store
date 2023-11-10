class RegistrationPage:
    def __init__(self, page):
        self.page = page
        self._first_name = page.locator('//*[@id="AccountFrm_firstname"]')
        self._last_name = page.locator('//*[@id="AccountFrm_lastname"]')
        self._email = page.locator('//*[@id="AccountFrm_email"]')
        self._address = page.locator('//*[@id="AccountFrm_address_1"]')
        self._city = page.locator('//*[@id="AccountFrm_city"]')
        self._region = page.locator("#AccountFrm_zone_id")#('//*[@id="AccountFrm_zone_id"]')
        self._zip_code = page.locator('//*[@id="AccountFrm_postcode"]')
        self._login_name = page.locator('//*[@id="AccountFrm_loginname"]')
        self._password = page.locator('//*[@id="AccountFrm_password"]')
        self._confirm_password = page.locator('//*[@id="AccountFrm_confirm"]')
        self._accept_policy = page.get_by_label("I have read and agree to the Privacy Policy")
        self._accept_policy2 = page.locator('//*[@id="AccountFrm_agree"]')
        self._register_button = page.locator('//*[@id="AccountFrm"]/div[5]/div/div/button')
        self._error_message = page.locator('//*[@id="maincontainer"]/div/div/div/div[1]')

    def enter_first_name(self, first_name):
        self._first_name.clear()
        self._first_name.fill(first_name)

    def enter_last_name(self, last_name):
        self._last_name.clear()
        self._last_name.fill(last_name)

    def enter_email(self, email):
        self._email.clear()
        self._email.fill(email)

    def enter_full_address(self, full_address):
        self._address.clear()
        self._address.fill(full_address)

    def enter_city(self, city):
        self._city.clear()
        self._city.fill(city)

    def enter_region(self, region):
        self._region.select_option(region)

    def enter_zip_code(self, zip_code):
        self._zip_code.clear()
        self._zip_code.fill(zip_code)

    def enter_login_name(self, login_name):
        self._login_name.clear()
        self._login_name.fill(login_name)

    def enter_password(self, password):
        self._password.clear()
        self._password.fill(password)

    def enter_confirm_password(self, confirm_password):
        self._confirm_password.clear()
        self._confirm_password.fill(confirm_password)

    def accept_policy_checkbox_check(self):
        self._accept_policy.check()

    def click_registration_button(self):
        self._register_button.click()

    def do_register_user(self, credentials):
        self.enter_first_name(credentials['first_name'])
        self.enter_last_name(credentials['last_name'])
        self.enter_email(credentials['email'])
        self.enter_full_address(credentials['full_address'])
        self.enter_city(credentials['city'])
        self.enter_region(credentials['region'])
        self.enter_zip_code(credentials['zip_code'])
        self.enter_login_name(credentials['login_name'])
        self.enter_password(credentials['password'])
        self.enter_confirm_password(credentials['password'])
        self.accept_policy_checkbox_check()
        self.click_registration_button()

    @property
    def error_message(self):
        return self._error_message
