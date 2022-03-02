from django.db import models


class Tiyatro(models.Model):
    stages = (
        ('publish', 'publish'),
        ('deleted', 'deleted')
    )
    title = models.CharField(verbose_name="Başlık", max_length=250)
    content = models.TextField(verbose_name="İçerik")
    video_url = models.CharField(verbose_name="Video Linki", max_length=250)
    status = models.CharField(choices=stages, default='publish', max_length=25, verbose_name="Statü")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")
