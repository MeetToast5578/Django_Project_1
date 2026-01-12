from django.db import models
from core.models import AbstractModel
from account.models import User
# from django.contrib.auth import get_user_model
# User = get_user_model()


# Create your models here.

class ProductTag(AbstractModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class ProductCategory(AbstractModel):

    parent = models.ForeignKey('self', related_name='child', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        if self.parent:
            return f'{self.parent} / {self.title}'
        return self.title
    

class Product(AbstractModel):
    category = models.ForeignKey(ProductCategory, related_name= 'products', on_delete=models.CASCADE)
    tags = models.ManyToManyField(ProductTag, related_name='products')

    title = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.category.title} / {self.title}'
    
    class Meta:
        ordering = ("-created_at",)
    

class ProductImage(AbstractModel):
    image = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title
    

class ProductReview(AbstractModel):

    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField()

    message = models.TextField()

    def __str__(self):
        return self.product.title
    
class ProductDiscount(AbstractModel):

    product = models.ForeignKey(Product, related_name='discounts', on_delete=models.CASCADE)
    discount_percent = models.FloatField()

    def __str__(self):
        return f'{self.product.title} / {self.discount_percent}'
    
class ProductColor(AbstractModel):
    product = models.ForeignKey(Product, related_name='colors', on_delete=models.CASCADE)
    color_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.product.title} / {self.color_name}'
    
class ProductSize(AbstractModel):
    product = models.ForeignKey(Product, related_name='sizes', on_delete=models.CASCADE)
    size_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.product.title} / {self.size_name}'