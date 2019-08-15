# Generated by Django 2.2.3 on 2019-08-02 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_music', '0004_auto_20190722_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='artist',
        ),
        migrations.AddField(
            model_name='tag',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_music.Album'),
        ),
    ]
