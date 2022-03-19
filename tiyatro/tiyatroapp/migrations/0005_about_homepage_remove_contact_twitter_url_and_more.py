# Generated by Django 4.0.3 on 2022-03-08 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiyatroapp', '0004_contact_tiyatro_theater_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Açıklama')),
                ('title', models.CharField(max_length=250, verbose_name='Başlık')),
                ('status', models.CharField(choices=[('publish', 'Yayınlandı'), ('deleted', 'Silindi')], default='publish', max_length=25, verbose_name='Statü')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Açıklama')),
                ('title', models.CharField(max_length=250, verbose_name='Başlık')),
                ('image_url', models.CharField(max_length=500, verbose_name='Resim Linki')),
                ('status', models.CharField(choices=[('publish', 'Yayınlandı'), ('deleted', 'Silindi')], default='publish', max_length=25, verbose_name='Statü')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='twitter_url',
        ),
        migrations.AddField(
            model_name='contact',
            name='instagram_url',
            field=models.CharField(max_length=250, null=True, verbose_name='Instagram Adresi'),
        ),
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[('publish', 'Yayınlandı'), ('deleted', 'Silindi')], default='publish', max_length=25, verbose_name='Statü'),
        ),
        migrations.AddField(
            model_name='tiyatro',
            name='image_url',
            field=models.CharField(max_length=500, null=True, verbose_name='Resim Linki'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='facebook_url',
            field=models.CharField(max_length=250, null=True, verbose_name='Facebook Adresi'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='youtube_url',
            field=models.CharField(max_length=250, null=True, verbose_name='Youtube Adresi'),
        ),
        migrations.AlterField(
            model_name='image',
            name='status',
            field=models.CharField(choices=[('publish', 'Yayınlandı'), ('deleted', 'Silindi')], default='publish', max_length=25, verbose_name='Statü'),
        ),
        migrations.AlterField(
            model_name='tiyatro',
            name='status',
            field=models.CharField(choices=[('publish', 'Yayınlandı'), ('deleted', 'Silindi')], default='publish', max_length=25, verbose_name='Statü'),
        ),
        migrations.AlterField(
            model_name='tiyatro',
            name='video_url',
            field=models.CharField(max_length=500, null=True, verbose_name='Video Linki'),
        ),
    ]