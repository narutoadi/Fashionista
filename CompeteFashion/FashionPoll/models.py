from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image
import random
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User) 
    #phone_number = models.CharField(max_length = 16, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",)], blank=True)
   	#picture = models.ImageField(upload_to = 'profile_images', blank=True)
	dob = models.DateField(blank=True)
	profile_picture=models.ImageField(upload_to='profile_images',blank=True, )
	phone_number = models.CharField(max_length=16,validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format '+9999999'. Upto 15 digits are allowed.")])

	def __unicode__(self):
		return self.user.username

class Fashionista(models.Model):
	user = models.OneToOneField(User)
	#Attributes of Fashionista
	fashionista_picture = models.ImageField(upload_to='fashionista_images',blank=False)
	title = models.CharField(max_length=250)
	likes = models.IntegerField(default=0)

	def random_photo(self):
    	#last = self.objects.count()-1
    	#index1 = random.randint(0, last)
		# Here's one simple way to keep even distribution for
		# index2 while still gauranteeing not to match index1.
		last = self.objects.count()-1
		index2 = random.randint(0, last - 1)
		index1 = random.randint(0, last)
		if index2 == index1: index2 = last
		MyObj1 = self.objects.all()[index1]
		MyObj2 = self.objects.all()[index2]
		return [MyObj1,MyObj2]

	def __unicode__(self):
		return self.user.username

