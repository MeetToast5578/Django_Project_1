from django.contrib import admin
from .models import ProductCategory, Product, ProductTag, ProductImage, ProductReview, ProductDiscount, ProductColor, ProductSize

# Register your models here.

admin.site.register(ProductCategory)

admin.site.register(ProductTag)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(ProductDiscount)
admin.site.register(ProductColor)
admin.site.register(ProductSize)


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'category']
    list_display_links = ['id', 'title']
    list_editable = ['category']
    readonly_fields = 'price',
    search_fields = ['title', 'description']
    list_filter = ['category', 'tags']
    # list_per_page = 2
    inlines = [ProductImageInline]
    