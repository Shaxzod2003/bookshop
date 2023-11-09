from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    username=models.CharField(max_length=64,unique=True)
    password=models.CharField(max_length=512)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) :
        return self.full_name
class Contact(models.Model):
    customer=models.OneToOneField(Customer, on_delete=models.CASCADE)
    email=models.EmailField()
    address=models.CharField(max_length=512)
    phone=models.CharField(max_length=13)
    def __str__(self):
        return f"{self.customer.full_name} - {self.phone}"