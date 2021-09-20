from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    unit = (
        ('Kg', 'Kg'),
        ('Piece', 'Piece'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()
    quantity = models.IntegerField(null=True, blank=True)
    unit_type = models.CharField(max_length=20, choices=unit, default="Select Quantity")
    photo = models.ImageField(upload_to='uploads/product', null=True, blank=True)


    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()


