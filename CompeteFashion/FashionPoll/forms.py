from django import forms
from django.contrib.auth.models import User
from FashionPoll.models import UserProfile, Fashionista

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('dob', 'profile_picture', 'phone_number')

class FashionistaForm(forms.ModelForm):
	class Meta:
		model = Fashionista
		fields = ('fashionista_picture', 'title')
