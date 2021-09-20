from django.contrib import admin
from django.urls import path
from core.views import Index, Products, ProductDetails
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="homepage"),
    path('product', Products.as_view(), name="product"),
    path('product/<int:pk>', ProductDetails.as_view(), name="product_details"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
