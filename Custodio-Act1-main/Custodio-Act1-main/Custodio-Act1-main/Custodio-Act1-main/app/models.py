from django.db import models
from django.urls import reverse

class Customer(models.Model):
    customerID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    productID = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE)
    orderDate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,
                              choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')])

    def __str__(self):
        return f"Order {self.orderID} by {self.customer}"

class Supplier(models.Model):
    supplierID = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    contact_email = models.EmailField(unique=True)
    contact_phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name