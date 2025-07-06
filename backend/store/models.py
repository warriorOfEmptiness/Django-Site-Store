from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=35)
    dsc = models.TextField(max_length=456,blank=True,null=True)

    def __str__(self):
        return self.name 



class Product(models.Model):
    name = models.CharField(max_length=156,unique=True)
    dsc = models.TextField(max_length=425)
    price = models.DecimalField(decimal_places=1,max_digits=7)
    image = models.ImageField(upload_to='catalog_images')

    def __str__(self):
        return f'{self.name} | {self.price}'
    


    
