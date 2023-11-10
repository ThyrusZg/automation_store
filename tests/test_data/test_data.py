class TestData:

    @staticmethod
    def valid_login_data():
        return {"username": "test_automation_user", "password": "1234"}

    @staticmethod
    def invalid_login_data():
        return {"username": "none", "password": "none"}

    @staticmethod
    def valid_register_data():
        return {"first_name": "test", "last_name": "test", "email": "tes1212t@mail.com", "full_address": "ilica",
                "city": "zagreb", "region": "3513", "zip_code": "12345", "login_name": "new_tester_123",
                "password": "abcd1234"}

    @staticmethod
    def string_test():
        return "test"

    @staticmethod
    def link_text():
        return "link"

    @staticmethod
    def span_maintext():
        return "span.maintext"

    @staticmethod
    def span_bgnone():
        return "span.bgnone"

    @staticmethod
    def account_created_text():
        return "Your Account Has Been Created!"

    @staticmethod
    def my_account_text():
        return "My Account"

    @staticmethod
    def account_login_text():
        return "Account Login"

    @staticmethod
    def create_account_text():
        return "Create Account"

    @staticmethod
    def search_text():
        return "Search"

    @staticmethod
    def shopping_cart():
        return "Shopping Cart"
    """
    PRODUCTS
    """
    @staticmethod
    def waterproof_protective_undereye_concealer():
        return "Waterproof Protective Undereye Concealer"

    @staticmethod
    def total_moisture_facial_cream():
        return "Total Moisture Facial Cream"

    @staticmethod
    def jersey_cotton_striped_polo_shirt():
        return "Jersey Cotton Striped Polo Shirt"

    @staticmethod
    def polo_text():
        return "polo"

    @staticmethod
    def cream_precieuse_nut():
        return "Creme Precieuse Nuit 50ml"

    @staticmethod
    def gucci_guilty():
        return "Gucci Guilty"

    @staticmethod
    def shower_text():
        return "shower"

    @staticmethod
    def men_plus_care_shower_tool():
        return "Men+Care Active Clean Shower Tool"

    @staticmethod
    def eau_text():
        return "eau"

    @staticmethod
    def eau_parfumee_au_the_vert_shampoo():
        return "Eau Parfumee au The Vert Shampoo"

    @staticmethod
    def allegiant_by_veronica_roth():
        return "Allegiant by Veronica Roth"
