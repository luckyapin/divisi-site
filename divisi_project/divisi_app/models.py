from django.db import models
from django.urls import reverse
# Create your models here.



class Divisi_User(models.Model):
    login = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    index = models.IntegerField()
    def __str__(self):
        return self.login
    
class Cart(models.Model):
    login = models.ForeignKey("Divisi_User", on_delete=models.PROTECT)
    product = models.ForeignKey("Products", on_delete=models.PROTECT)
    quantity = models.IntegerField()

class Products(models.Model):
    name = models.SlugField(max_length=255, unique=True, db_index=True)
    cost = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    available = models.BooleanField(default=True)
    def get_absolute_url(self):
        return reverse('product', kwargs={"product_id": self.id})

class Category(models.Model):
    category = models.CharField( max_length=255)
    def __str__(self):
        return self.category
    
def photo_directory_path(instance, filename):
    print(instance.product)
    print(filename)
    return 'photo/{0}/{1}'.format(instance.product.pk, filename)

class Photos(models.Model):
    product = models.ForeignKey('Products', on_delete=models.PROTECT)
    photo = models.ImageField(upload_to=photo_directory_path, verbose_name='Фото')
