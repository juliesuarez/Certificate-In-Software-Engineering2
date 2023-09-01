from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=100,null=False,blank=False)
    last_name = models.CharField(max_length=100,null=False,blank=False)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100,null=False,blank=False)
    district = models.CharField(max_length=50,null=False,blank=False)
    country = models.CharField(max_length=50,null=False,blank=False)
    town_zip_code = models.IntegerField(default=0,null=False,blank=False)
    phone_number1 = models.CharField(max_length=20,null=False,blank=False)
    phone_number2 = models.CharField(max_length=20,null=False,blank=False)
    email = models.EmailField()
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"