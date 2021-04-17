from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	usertype = models.CharField(max_length=30)
	gender=models.CharField(max_length=10)
	address=models.CharField(max_length=200)
	laptop=models.CharField(max_length=10)
	mobile=models.CharField(max_length=200)
	dob=models.DateField()
	parentname=models.CharField(max_length=100)


class student(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)


class teacher(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	
		

	

		