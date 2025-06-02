from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class DigitValidator(BaseValidator):
    message = "National number should only contain digits."
    code = "digits_only"

    def compare(self, value, limit_value):
        return not value.isdigit()


@deconstructible
class LengthValidator(BaseValidator):
    message = "National number should be exactly 11 digits long."
    code = "length_11"

    def compare(self, value, limit_value):
        return len(value) != 11


@deconstructible
class StringValidator(BaseValidator):
    message = "names should only be string and can't contain numbers."
    code = "strings_only"

    def compare(self, value, limit_value):
        return value.isdigit()
