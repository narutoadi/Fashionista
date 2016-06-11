from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image
import random
# Model to maintain user data other then what is offered by django.contrib.auth.models
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	dob = models.DateField(blank=True)
	profile_picture=models.ImageField(upload_to='profile_images',blank=True,)
	phone_number = models.CharField(max_length=16,validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format '+9999999'. Upto 15 digits are allowed.")])

	def __str__(self):
		return self.user.username

# Model to maintain each participant's data
class Fashionista(models.Model):
	user = models.OneToOneField(User)
	fashionista_picture = models.ImageField(upload_to='fashionista_images',blank=False)
	title = models.CharField(max_length=250)
	likes = models.IntegerField(default=0)
	views = models.IntegerField(default=0)
	rating = models.FloatField(default = 1000.0000, db_index = True)

	def random_photo(self):
		last = self.objects.count()-1
		index2 = random.randint(0, last - 1)
		index1 = random.randint(0, last)
		if index2 == index1: index2 = last
		MyObj1 = self.objects.all()[index1]
		MyObj2 = self.objects.all()[index2]
		return [MyObj1,MyObj2]

	def __unicode__(self):
		return self.user.username

#Model to maintain random pairs 
class Order(models.Model):
    liker = models.ForeignKey(User, null=False, related_name='liker')
    liked = models.ForeignKey(User, null=False, related_name='liked')
    unliked = models.ForeignKey(User, null=False, related_name='unliked')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        index_together = ["liker", "created_at"],