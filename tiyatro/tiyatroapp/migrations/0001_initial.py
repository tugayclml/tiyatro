# Generated by Django 4.0.3 on 2022-03-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tiyatro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Başlık')),
                ('content', models.TextField(verbose_name='İçerik')),
                ('video_url', models.CharField(max_length=250, verbose_name='Video Linki')),
                ('status', models.CharField(choices=[('publish', 'publish'), ('deleted', 'deleted')], default='publish', max_length=25, verbose_name='Statü')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')),
            ],
        ),
    ]
