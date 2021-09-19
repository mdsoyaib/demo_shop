from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse

# Create your views here.
from core.models import Product, Category


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class Products(View):
    def get(self, request):
        category = Category.objects.all()
        product = Product.objects.all()

        return render(request, 'product.html', {'products': product, 'category': category})


class ProductDetails(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        return render(request, 'product_details.html', {'product': product})