# Generated by Django 4.0.3 on 2022-03-05 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiyatroapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Başlık')),
                ('description', models.CharField(max_length=150, verbose_name='Açıklama')),
                ('image_url', models.CharField(max_length=500, verbose_name='Resim Linki')),
                ('status', models.CharField(choices=[('publish', 'publish'), ('deleted', 'deleted')], default='publish', max_length=25, verbose_name='Statü')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')),
            ],
        ),
        migrations.AlterField(
            model_name='tiyatro',
            name='video_url',
            field=models.CharField(max_length=500, verbose_name='Video Linki'),
        ),
    ]
