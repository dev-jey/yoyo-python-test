from django.urls import path

from yoyo_app.temperature_api.views import TemperatureView

urlpatterns = [
    path('<str:city>/', TemperatureView.as_view(), name="temperature"),
]
