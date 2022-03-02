from django.urls import path

from .views import TiyatroAPIView


urlpatterns = [
    path('tiyatro', TiyatroAPIView.as_view({"get": "list"})),
]
