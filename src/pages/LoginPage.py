from automation_store.src.pages import AccountPage


class LoginPage:
    def __init__(self, page):
        self.page = page
        self._username = page.locator("#loginFrm_loginname")
        self._password = page.locator("#loginFrm_password")
        self._login_button = page.get_by_role("button", name=" Login")

    def enter_username(self, username):
        self._username.clear()
        self._username.fill(username)

    def enter_password(self, password):
        self._password.clear()
        self._password.fill(password)

    def click_login_button(self):
        self._login_button.click()

    def do_login(self, credentials):
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])
        self.click_login_button()
        return AccountPage(self.page)
