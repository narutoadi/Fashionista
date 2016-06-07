from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from FashionPoll.forms import UserForm, UserProfileForm, FashionistaForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from FashionPoll.models import Fashionista, UserProfile
# Create your views here.
def index(request):
	context_dict = {'boldmessage' : "I am bold font from the context"}
	return render(request, 'FashionPoll/index.html', context_dict)

def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_picture' in request.FILES:
				profile.profile_picture = request.FILES['profile_picture']

			profile.save()

			registered = True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,
		'FashionPoll/register.html',
		{'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/FashionPoll/home/')
			else:
				return HttpResponse("Your account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username,password))
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'FashionPoll/login.html', {})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/FashionPoll/')

def home(request):
	profile = UserProfile.objects.filter(user=request.user)[:1]
	participation = Fashionista.objects.filter(user=request.user)[:1]
	fashionista_list = Fashionista.objects.order_by('?')[:2]
	context_dict = {'fList' : fashionista_list, 'uprofile' : profile, 'uparticipation' : participation, }
	return render(request, 'FashionPoll/home.html', context_dict)

def participate(request):
	registered = False
	if request.method == 'POST':
		fashionista_form = FashionistaForm(data = request.POST)

		if fashionista_form.is_valid():
			fashionista = fashionista_form.save(commit=False)
			fashionista.user = user

			if 'fashionista_picture' in request.FILES:
				fashionista.fashionista_picture = request.FILES['fashionista_picture']

			fashionista.save()

			registered = True

		else:
			print(fashionista_form.errors)

	else:
		fashionista_form = FashionistaForm()

	return render(request,
		'FashionPoll/participate.html',
		{'fashionista_form': fashionista_form, 'registered': registered} )
