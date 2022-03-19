from rest_framework import viewsets
from rest_framework.response import Response

from .models import Tiyatro, Image, Contact, About, HomePage
from .serializer import TiyatroSerializer, ImageSerializer, ContactSerializer, AboutSerializer, HomePageSerializer


class TiyatroAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = Tiyatro.objects.all()
        serializer = TiyatroSerializer(queryset, many=True)
        return Response(serializer.data)


class ImageAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = Image.objects.all()
        serializer = ImageSerializer(queryset, many=True)
        return Response(serializer.data)


class ContactAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = Contact.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)


class AboutAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = About.objects.all()
        serializer = AboutSerializer(queryset, many=True)
        return Response(serializer.data)


class HomePageAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = HomePage.objects.all()
        serializer = HomePageSerializer(queryset, many=True)
        return Response(serializer.data)

