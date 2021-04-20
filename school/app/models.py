from django.db import models

# Create your models here.
class UserInformation(models.Model):
    nik = models.IntegerField(primary_key=True)
    nama_pendek = models.CharField(max_length=100, null=True)
    nama_panjang = models.CharField(max_length=100, null=True)
    jabatan = models.CharField(max_length=100, null=True)
    alamat = models.CharField(max_length=200, null=True)
    nomor_telepon = models.IntegerField()

class Laporan(models.Model):
    ZONA = (
        ('Barat','Barat'),
        ('Utara','Utara'),
        ('Timur','Timur'),
        ('Selatan','Selatan'),
        )

    JENIS = (
        ('Persil','Persil'),
        ('Trandist','Trandist')
    )

    STATUS = (
        ('Pending','Pending'),
        ('Penanganan','Penanganan'),
        ('Selesai','Selesai'),
    )

    spk = models.IntegerField(primary_key=True)
    zona = models.CharField(max_length=200, null=True, choices=ZONA)
    nama = models.CharField(max_length=200, null=True)
    alamat = models.CharField(max_length=200, null=True)
    tanggal = models.DateField(null=True)
    gangguan = models.CharField(max_length=200, null=True)
    jenis = models.CharField(max_length=200, null=True, choices=JENIS)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
       return self.nama