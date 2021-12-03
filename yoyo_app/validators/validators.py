import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def _has_special_chars(value):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(value):
        raise ValidationError(
            _('%(value)s cannot contain special characters'),
            params={'value': value},
        )


def _is_between_1_and_10(value):
    if value.isnumeric():
        if not (int(value) <= 10 and int(value) > 0):
            raise ValidationError(
                _('%(value)s must be between 1 and 10'),
                params={'value': value},
            )
    else:
        raise ValidationError(
            _('%(value)s must be an integer'),
            params={'value': value},
        )
