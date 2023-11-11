class TestData:

    @staticmethod
    def valid_login_data():
        return {"username": "test_automation_user", "password": "1234"}

    @staticmethod
    def invalid_login_data():
        return {"username": "none", "password": "none"}

    @staticmethod
    def valid_register_data():
        return {"first_name": "test", "last_name": "test", "email": "tes12121212t@mail.com", "full_address": "ilica",
                "city": "zagreb", "region": "3513", "zip_code": "12345", "login_name": "new_1tester_12345",
                "password": "abcd1234"}

    @staticmethod
    def valid_username():
        return "test_automation_user"

    @staticmethod
    def invalid_username():
        return "no"

    @staticmethod
    def valid_password():
        return "1234"

    @staticmethod
    def invalid_password():
        return "no"

    @staticmethod
    def home_page():
        return "https://automationteststore.com/"

    @staticmethod
    def string_test():
        return "test"

    @staticmethod
    def link_text():
        return "link"

    @staticmethod
    def contentpanel_text():
        return '//*[@id="maincontainer"]/div/div/div/div'

    @staticmethod
    def span_maintext():
        return "span.maintext"

    @staticmethod
    def span_bgnone():
        return "span.bgnone"

    @staticmethod
    def span_nostock():
        return "span.nostock"

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

    @staticmethod
    def out_of_stock_text():
        return "Out of Stock"

    @staticmethod
    def checkout_confirmation_text():
        return "Checkout Confirmation"

    @staticmethod
    def delivery_information_text():
        return "Delivery Information"

    @staticmethod
    def shipping_address_text():
        return "Shipping Address"

    @staticmethod
    def payment_information_text():
        return "Payment Information"

    @staticmethod
    def payment_address_text():
        return "Payment Address"

    @staticmethod
    def processed_order_text():
        return "Your Order Has Been Processed!"

    @staticmethod
    def invoice_order_text():
        return "Order Details"

    @staticmethod
    def your_shopping_cart_is_empty_text():
        return "Your shopping cart is empty!"
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

    @staticmethod
    def skinsheen_bronzer_stick():
        return "Skinsheen Bronzer Stick"
