"""Global validators that can be used in any app within the project."""
import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

pattern = '[@_!#$%^&*()<>?/\|}{~:]'


def _has_special_chars(value):
    """Check if value contains a special character."""
    regex = re.compile(pattern)
    if regex.search(value):
        raise ValidationError(
            _('%(value)s cannot contain special characters'),
            params={'value': value},
        )


def _is_between_1_and_10(value):
    """Check if value is alphanumeric, and between 1 and 10."""
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
