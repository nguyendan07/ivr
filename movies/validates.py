from django.conf import settings
from django.core.exceptions import SuspiciousOperation
from django.http import HttpRequest
from twilio.request_validator import RequestValidator

request_validator = RequestValidator(settings.TWILIO_AUTH_TOKEN)


def validate_django_request(request):
    try:
        signature = request.META['HTTP_X_TWILIO_SIGNATURE']
    except KeyError:
        is_valid_twilio_request = False
    else:
        is_valid_twilio_request = request_validator.validate(
            signature = signature,
            uri = request.get_raw_uri(),
            params = request.POST,
        )
    if not is_valid_twilio_request:
        raise SuspiciousOperation()
