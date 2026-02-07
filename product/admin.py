from django.contrib import admin
from .models import ProductCategory, Product, ProductTag, ProductImage, ProductReview, ProductDiscount, ProductColor, ProductSize
from modeltranslation.admin import TranslationAdmin
# Register your models here.


class ProductTagAdmin(TranslationAdmin):
    list_display = 'title',
admin.site.register(ProductTag)

class ProductCategoryAdmin(TranslationAdmin):
    list_display = 'title',
admin.site.register(ProductCategory)


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
    