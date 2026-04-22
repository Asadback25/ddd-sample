from random import randint

class OTPService:
    @staticmethod
    def generate_otp():
        return str(randint(111111, 999999))