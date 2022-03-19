from django.db import models


class Tiyatro(models.Model):
    stages = (
        ('publish', 'Yayınlandı'),
        ('deleted', 'Silindi')
    )
    title = models.CharField(verbose_name="Başlık", max_length=250)
    content = models.TextField(verbose_name="İçerik")
    video_url = models.CharField(verbose_name="Video Linki", max_length=500, null=True)
    image_url = models.CharField(verbose_name="Resim Linki", max_length=500, null=True)
    theater_date = models.DateTimeField(verbose_name="Tembihname Tarihi", null=True)
    status = models.CharField(choices=stages, default='publish', max_length=25, verbose_name="Statü")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")

    class Meta:
        verbose_name_plural = "Tiyatrolar"


class Image(models.Model):
    stages = (
        ('publish', 'Yayınlandı'),
        ('deleted', 'Silindi')
    )
    title = models.CharField(verbose_name="Başlık", max_length=250)
    description = models.CharField(verbose_name="Açıklama", max_length=150)
    image_url = models.CharField(verbose_name="Resim Linki", max_length=500)
    status = models.CharField(choices=stages, default='publish', max_length=25, verbose_name="Statü")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")


    class Meta:
        verbose_name_plural = "Fotoğraflar"


class Contact(models.Model):
    stages = (
        ('publish', 'Yayınlandı'),
        ('deleted', 'Silindi')
    )
    address = models.TextField(verbose_name="Adres")
    email = models.CharField(verbose_name="Email", max_length=100)
    phone_number = models.CharField(verbose_name="Telefon Numarası", max_length=11)
    facebook_url = models.CharField(verbose_name="Facebook Adresi", max_length=250, null=True)
    instagram_url = models.CharField(verbose_name="Instagram Adresi", max_length=250, null=True)
    youtube_url = models.CharField(verbose_name="Youtube Adresi", max_length=250, null=True)
    status = models.CharField(choices=stages, default='publish', max_length=25, verbose_name="Statü")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")

    class Meta:
        verbose_name_plural = "İletişim"


class About(models.Model):
    stages = (
        ('publish', 'Yayınlandı'),
        ('deleted', 'Silindi')
    )
    description = models.TextField(verbose_name="Açıklama")
    title = models.CharField(verbose_name="Başlık", max_length=250)
    status = models.CharField(choices=stages, default='publish', max_length=25, verbose_name="Statü")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Hakkımızda"


class Card(models.Model):
    stages = (
        ('publish', 'Yayınlandı'),
        ('deleted', 'Silindi')
    )
    number = models.IntegerField(verbose_name="Sayi")
    label = models.CharField(verbose_name="Etiket", max_length=250)
    about = models.ForeignKey(About, related_name="cards", on_delete=models.CASCADE, null=True)
    status = models.CharField(choices=stages, default='publish', max_length=25, verbose_name="Statü")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")

    class Meta:
        verbose_name_plural = "Kartlar"


class HomePage(models.Model):
    stages = (
        ('publish', 'Yayınlandı'),
        ('deleted', 'Silindi')
    )
    description = models.TextField(verbose_name="Açıklama")
    title = models.CharField(verbose_name="Başlık", max_length=250)
    image_url = models.CharField(verbose_name="Resim Linki", max_length=500)
    status = models.CharField(choices=stages, default='publish', max_length=25, verbose_name="Statü")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")

    class Meta:
        verbose_name_plural = "Anasayfa"
