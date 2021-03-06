from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete
# Create your models here.

class Category(models.Model):
    title= models.CharField(max_length = 200)
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    name=models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=7,decimal_places=2,default = 0.00)
    image = models.ImageField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")

    def __str__(self):
        return self.name


#Model that represents the relationship between order and product
class OrderProduct(models.Model):
    order = models.ForeignKey("Order", on_delete = models.CASCADE,related_name='orders',null=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE,related_name='orders')
    quantity = models.PositiveIntegerField(default=1)
    quantity_price = models.DecimalField(max_digits=7, null=True, decimal_places=2,default=0.00)
    
    def __str__(self):
        return f'order of {self.product.name} in order #{self.order.id} of quantity{self.quantity}'

class Order(models.Model):
    user= models.ForeignKey(User, on_delete = models.CASCADE ,null=True)
    is_current = models.BooleanField(default = False)
    date_time = models.DateTimeField(auto_now_add=True) 
    products = models.ManyToManyField(Product, through = OrderProduct)
    total_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.user.username}\'s order #{self.id} with total of {self.total_cost}'
    
    def total(self):
        self.total_cost = sum(self.orders.all().values_list('quantity_price', flat=True))
        self.save()


@receiver(pre_save, sender = OrderProduct)
def get_quantity_price(instance, *args, **kwargs):
	instance.quantity_price = instance.product.price*instance.quantity


@receiver(post_save, sender=OrderProduct)
def total(sender, instance, *args, **kwargs):
    instance.order.total()

