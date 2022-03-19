from django.urls import path

from .views import TiyatroAPIView, ImageAPIView, ContactAPIView, AboutAPIView, HomePageAPIView


urlpatterns = [
    path('theaters', TiyatroAPIView.as_view({"get": "list"})),
    path('images', ImageAPIView.as_view({"get": "list"})),
    path('contact', ContactAPIView.as_view({"get": "list"})),
    path('about', AboutAPIView.as_view({"get": "list"})),
    path('homepage', HomePageAPIView.as_view({"get": "list"})),
]
