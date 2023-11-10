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
    def waterproof_protective_undereye_concealer():
        return "Waterproof Protective Undereye Concealer"

    @staticmethod
    def total_moisture_facial_cream():
        return "Total Moisture Facial Cream"

