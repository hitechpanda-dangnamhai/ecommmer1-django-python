from django.db import models
from django.urls import reverse
from category.models import Category

import uuid

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to = 'photos/products', default = 'default.png')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    #id = models.UUIDField(default = uuid.uuid4, unique= True, primary_key=True, editable=False)
    

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


#hàm này chỉ có tác dụng lọc, rất hay
class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color',is_active= True )
    def sizes(self):
        return super(VariationManager,self).filter(variation_category='size', is_active = True)

class Variation(models.Model):
    variation_category_choice = (
    ('color','color'),
    ('size', 'size'),)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now = True)

    objects = VariationManager() # coi nhu doi tuong

    def __str__(self):
        return self.variation_value
 