from product.models import ProductCategory, Product
from core.models import Subscribe
from django.http import JsonResponse
from product.api.serializers import (
    ProductCategorySerializer,
    ProductSerializer,
    ProductCreateSerializer,
    SubscribeSerializer,
)
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView


class SubscriberAPIView(CreateAPIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()

def categories(request):
    categories = ProductCategory.objects.all()
    serializer = ProductCategorySerializer(categories, many = True)
    # category_dict = []
    # for category in categories:
    #     if category.parent:
    #         category_dict.append(
    #             {
    #                 'parent' : category.parent.id,
    #                 'id' : category.id,
    #                 'title': category.title
    #             }
    #         )
    #     else:
    #         category_dict.append(
    #             {
    #                 'id' : category.id,
    #                 'title': category.title
    #             }
    #         )
    return JsonResponse(data = serializer.data, safe= False)



@api_view(http_method_names=["GET", "POST"])
def products(request):
    products = Product.objects.all()
    if request.method == "POST":
        serializer = ProductCreateSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status=201)
        return JsonResponse(data=serializer.errors, safe=False, status=400)
    serializer = ProductSerializer(products, context={"request": request}, many=True)
    return JsonResponse(data=serializer.data, safe=False)


@api_view(http_method_names=["PUT", "PATCH"])
def product_update(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "PUT":
        serializer = ProductCreateSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status=201)
        return JsonResponse(data=serializer.errors, safe=False, status=400)
    if request.method == "PATCH":
        serializer = ProductCreateSerializer(
            instance=product, partial=True, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status=201)
        return JsonResponse(data=serializer.errors, safe=False, status=400)
    serializer = ProductSerializer(products, context={"request": request}, many=True)
    return JsonResponse(data=serializer.data, safe=False)


class ProductListAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductCreateSerializer
        return super().get_serializer_class()


class ProductUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()