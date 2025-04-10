from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class RegisterModel(models.Model):
    class Gender(models.TextChoices):
        MALE='male','Male'
        FEMALE='female','Female'
        OTHER='other','Other'

    phone_regex = RegexValidator(
        regex=r'^\d{10,15}$',  # Allows only numbers, length 10-15
        message="Phone number must be 10-15 digits long."
    )

    firstName = models.CharField(verbose_name="First Name: ",max_length=64)
    lastName = models.CharField(verbose_name="Last Name: ",max_length=64)
    userEmail = models.EmailField(verbose_name="Email Address: ",max_length=64)
    userPswd = models.CharField(verbose_name="Password: ",max_length=64)
    gender = models.CharField(verbose_name="Gender: ",max_length=6,choices=Gender.choices,blank=False)
    phoneNumber = models.CharField(verbose_name="Phone Number: ",max_length=15, validators=[phone_regex])