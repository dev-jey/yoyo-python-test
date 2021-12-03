from rest_framework import serializers

from yoyo_app.helpers.validators import (
    _has_special_chars, _is_between_1_and_10, _is_string)


class TemperatureSerializer(serializers.Serializer):
    maximum = serializers.IntegerField(read_only=True)
    minimum = serializers.IntegerField(read_only=True)
    average = serializers.IntegerField(read_only=True)
    median = serializers.IntegerField(read_only=True)
    days = serializers.CharField(
        max_length=30, allow_null=False,
        allow_blank=False, validators=[_is_string, _is_between_1_and_10])
    city = serializers.CharField(
        max_length=30, allow_null=False,
        allow_blank=False, validators=[_has_special_chars])
