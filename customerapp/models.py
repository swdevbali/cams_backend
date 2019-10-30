from django.db import models


class Vehicle(models.Model):
    """
    Harusnya dibagi menjadi merk dan tipe
    Gambar skip.
    """
    nama = models.fields.CharField(max_length=255)
    harga = models.fields.FloatField()

    def __str__(self):
        return self.nama

    def __repr__(self):
        return self.nama

JENIS_KELAMIN = (
    ('L', 'Laki-Laki'),
    ('P', 'Perempuan'),
)

OCCUPATION = (
    ('n', 'Non-Fix'),
    ('f', 'Fix')
)
# Create your models here.
class Customer(models.Model):
    nama = models.fields.CharField(max_length=255)
    jenis_kelamin = models.fields.CharField(max_length=1, choices=JENIS_KELAMIN, default='L')
    gaji = models.fields.FloatField()
    existing = models.fields.BooleanField()
    occupation = models.fields.CharField(max_length=1, choices=OCCUPATION, default='n') # FIX, NONFIX
    alamat = models.fields.TextField()
    kendaraan = models.ManyToManyField(Vehicle)

    def __str__(self):
        return self.nama

    def __repr__(self):
        return self.nama
