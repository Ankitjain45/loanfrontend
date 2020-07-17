from django.db import models


# Create your models here.

class Userdetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    aadhar = models.IntegerField()
    pan = models.IntegerField()
    address = models.CharField(max_length=700)
    loan_amount = models.IntegerField()
    reason = models.CharField(max_length=1000)
    apply_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
