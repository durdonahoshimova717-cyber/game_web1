from django.db import models


class Mahsulot(models.Model):
    nomi=models.CharField(255)
    narxi=models.DecimalField(max_digits=10,decimal_places=2)
    sharhi=models.TextField()
    rasm=models.ImageField(upload_to='mahsulot/')
    def __str__(self):
        return self.nomi

class Haqida(models.Model):
    sarlavha=models.CharField(255)
    matn=models.TextField()
    rasm=models.ImageField(upload_to='haqida/')
    def __str__(self):
        return self.sarlavha

class Product(models.Model):
    nomi=models.CharField(255)
    narxi=models.DecimalField(max_digits=10,decimal_places=2)
    rasm=models.ImageField(upload_to='product/')
    def __str__(self):
        return self.nomi


class Reklama(models.Model):
    kichik_sarlavha=models.CharField(max_length=255)
    matn=models.TextField()
    rasm=models.ImageField(upload_to='reklama/')
    def __str__(self):
        return self.kichik_sarlavha



