from django.conf import settings
from django.core.mail import send_mail


def send_mail_task(email, otp):
    send_mail(
        subject='Verify OTP',
        message=f'Verify your OTP using this code: {otp}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
    )