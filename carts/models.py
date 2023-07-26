from django.db import models
from store.models import Product
from store.models import Variation

# Create your models here.
class Cart(models.Model):
    carts_id=models.CharField(max_length=200,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.carts_id
    
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation,blank=True)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    is_active=models.BooleanField(default=True)

    def __unicode__(self):
        return self.product
    
    def sub_total(self):
        return self.product.price * self.quantity
