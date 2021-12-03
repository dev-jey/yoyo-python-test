from rest_framework import serializers
from temperature.validators import _has_special_chars, _is_string
from django.utils.translation import gettext_lazy as _


class TemperatureSerializer(serializers.Serializer):
    maximum = serializers.IntegerField(read_only=True)
    minimum = serializers.IntegerField(read_only=True)
    average = serializers.IntegerField(read_only=True)
    median = serializers.IntegerField(read_only=True)
    days = serializers.CharField(
        max_length=30, allow_null=False, allow_blank=False, validators=[_is_string])
    city = serializers.CharField(
        max_length=30, allow_null=False, allow_blank=False, validators=[_has_special_chars])
