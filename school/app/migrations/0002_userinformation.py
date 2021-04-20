# Generated by Django 3.1.7 on 2021-04-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('nik', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_pendek', models.CharField(max_length=100, null=True)),
                ('nama_panjang', models.CharField(max_length=100, null=True)),
                ('jabatan', models.CharField(max_length=100, null=True)),
                ('alamat', models.CharField(max_length=200, null=True)),
                ('nomor_telepon', models.IntegerField()),
            ],
        ),
    ]