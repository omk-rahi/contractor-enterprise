import random
from datetime import timedelta
from django.utils.timezone import now

from .models import OTP

def generate_and_save_otp(user):

    otp_code = str(random.randint(100000, 999999))

    expiration_time = now() + timedelta(minutes=5)
    
    otp = OTP.objects.create(user=user, code=otp_code, expires_at=expiration_time)

    return otp


def verify_otp(user, otp_input):



    try:
        otp = OTP.objects.filter(user=user).latest('created_at')

        if otp.code == otp_input and otp.is_valid():
            return True
        return False
    except OTP.DoesNotExist:
        return False
