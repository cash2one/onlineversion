from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class ProductSet(models.Model):
    ProductGroup = models.IntegerField()
    ProductSetName = models.CharField(max_length=200)
    ProductSetStatus = models.IntegerField()

    def __unicode__(self):
        return self.id
    class Meta:
        db_table="ProductSet"


class Product(models.Model):
    ProductGroup = models.IntegerField()
    ProductSetId = models.ForeignKey(ProductSet)
    ProductName = models.CharField(max_length=200)
    ProductNameReg = models.CharField(max_length=200)
    ProductSvnReg = models.CharField(max_length=200)
    ProductStatus = models.IntegerField()

    def __unicode__(self):
        return self.ProductName
    class Meta:
        db_table="Product"






