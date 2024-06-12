from django.db import models

# Create your models here.

class Product(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'


    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold')
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6 , decimal_places=2)  #always use DecimalField on monatory values as FloatField has rounding issues.  
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

class Customer(models.Model):
    first_name = models.Charfield(max_length=255)
    last_name = models.Charfield(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.Charfield(max_length=255)
    birth_date = models.DateField(null=True)

class order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_CHOICES = [
        (PAYMENT_PENDING , 'Pending'),
        (PAYMENT_COMPLETE, 'Complete'),
        (PAYMENT_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.Charfield(max_lenght=1, choices=PAYMENT_CHOICES, default=PAYMENT_PENDING)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OnetoOneField(Customer, on_delete=models.CASCADE, primary_key=True)