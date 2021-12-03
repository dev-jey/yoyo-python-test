from django.urls import path
from temperature.views import TemperatureView

urlpatterns = [
    path('<str:city>/', TemperatureView.as_view(), name="temperature"),
]
