from modeltranslation.translator import translator, TranslationOptions
from product.models import ProductTag, ProductCategory

class ProductTagTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(ProductTag, ProductTagTranslationOptions)


class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(ProductCategory, ProductCategoryTranslationOptions)