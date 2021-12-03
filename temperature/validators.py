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


def _is_string(value):
    if not value.isnumeric():
        raise ValidationError(
            _('%(value)s must be an integer'),
            params={'value': value},
        )
