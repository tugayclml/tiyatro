from django.contrib import admin

from .models import Tiyatro, Image, Contact, About, HomePage, Card


@admin.register(Tiyatro)
class TiyatroAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content', 'video_url']
    list_display = ('id', 'title', 'content', 'theater_date', 'video_url', 'image_url', 'status', 'created_at', 'updated_at')


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'image_url']
    list_display = ('id', 'title', 'description', 'image_url', 'status', 'created_at', 'updated_at')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ['address', 'email', 'phone_number', 'facebook_url', 'twitter_url', 'youtube_url']
    list_display = ('id', 'address', 'email', 'phone_number', 'facebook_url', 'instagram_url', 'youtube_url', 'status', 'created_at', 'updated_at')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    search_fields = ['label']
    list_display = ('id', 'label', 'number')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description')
    list_display = ('id', 'title', 'description', 'status', 'created_at', 'updated_at')


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description', 'image_url')
    list_display = ('id', 'title', 'description', 'image_url', 'status', 'created_at', 'updated_at')
