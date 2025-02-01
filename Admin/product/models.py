from django.db import models


class Product(models.Model):
    Product_name = models.CharField(max_length=100, null=False)
    Product_discription = models.CharField(max_length=100)
    Product_image = models.ImageField(upload_to='media/image',default='')
    Product_price = models.IntegerField(default=0)
    Product_date = models.DateField()

    def __str__(self):
        return self.Product_name
