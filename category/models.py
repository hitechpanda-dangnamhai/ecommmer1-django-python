from django.db import models

from django.urls import reverse #
import uuid
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to = 'photos/categories', blank= True)
    id = models.UUIDField(default = uuid.uuid4, unique= True, primary_key=True, editable=False)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug]) 
            # products_by_category khai bao trong urls của ai cũng duoc
            # args=[self.slug] giá trị biến truyền vào
        
    def __str__(self):
        return self.category_name