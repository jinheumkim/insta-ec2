# Generated by Django 4.2.7 on 2023-12-14 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_delete_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='likecount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='feed',
            name='nickname',
            field=models.CharField(default='', max_length=24),
        ),
    ]