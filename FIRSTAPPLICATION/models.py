from django.db import models

# Create your models here.
# models.py

from django.db import models

class Name(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Contact(models.Model):
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    def __str__(self):
        return f"{self.phone_number} {self.email}"

class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50,default='',null= "")
    zip_code = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.street_address} {self.city} {self.state} {self.zip_code}"

