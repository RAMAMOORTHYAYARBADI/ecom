from django.db import models

# Create your models here.


class ProductMstr(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=512, null=True)
    product_code = models.CharField(max_length=64, null=True)
    product_image = models.CharField(max_length=1024, null=True)
    product_category = models.CharField(max_length=512, null=True)
    description  = models.TextField(null=True)
    product_price = models.DecimalField(default=0, max_digits = 10, decimal_places = 2)
    discount_price = models.DecimalField(default=0, max_digits = 10, decimal_places = 2)
    is_active = models.BooleanField(default=False)
    is_deleted= models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        managed = True
        db_table = 'product_mstr'