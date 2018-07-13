from django.db import models

# Create your models here.
class Volunteer_info(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	OTHER = 'O'
	NOSAY = 'N'
	GENDER_CHOICES=((MALE, 'Male'),(FEMALE, 'Female'),(OTHER, 'Other'),(NOSAY, 'Prefer not to say'))
	name=models.CharField(max_length=255)
	location=models.CharField(max_length=255)
	gender=models.CharField(max_length=255, choices=GENDER_CHOICES)

