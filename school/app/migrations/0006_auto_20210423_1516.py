# Generated by Django 3.1.7 on 2021-04-23 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210422_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
