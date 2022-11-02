# Generated by Django 3.2.13 on 2022-11-02 07:25

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_followings'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profileimg',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/profile/'),
        ),
    ]
