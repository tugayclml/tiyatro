from rest_framework import serializers
from .models import Tiyatro, Image, Contact, About, HomePage, Card


class TiyatroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiyatro
        fields = ('id', 'title', 'content', 'theater_date', 'video_url', 'image_url', 'status', 'created_at', 'updated_at')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'title', 'description', 'image_url', 'status', 'created_at', 'updated_at')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'address', 'email', 'phone_number', 'facebook_url', 'instagram_url', 'youtube_url', 'status', 'created_at', 'updated_at')


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'number', 'label')


class AboutSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)
    class Meta:
        model = About
        fields = ('id', 'title', 'description', 'cards', 'status', 'created_at', 'updated_at')


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = ('id', 'title', 'description', 'image_url', 'status', 'created_at', 'updated_at')

