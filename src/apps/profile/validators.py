import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def check_phone_number(value):
    pattern = r"^\+375(25|29|33|44)\d{7}$"
    match = re.match(pattern, value)
    if not match:
        raise ValidationError(
            _("%(value)s must look like +375(25|29|33|44)XXXXXXX (without brackets)"),
            params={"value": value},
        )
