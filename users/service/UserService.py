from users.tasks import send_mail_task
from users.service import OTPService
from django.contrib.auth.models import User
from django.db import transaction

class UserService:
    @staticmethod
    @transaction.atomic
    def create_user(username: str, email: str, password: str):
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.save()
        otp = OTPService.generate_otp()

        transaction.on_commit(lambda: send_mail_task(email, otp))
        return user

