# Generated by Django 3.2.13 on 2022-11-03 01:39

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_alter_restaurant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/restaurant/'),
        ),
    ]