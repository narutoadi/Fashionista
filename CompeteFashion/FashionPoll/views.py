from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from FashionPoll.forms import UserForm, UserProfileForm, FashionistaForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from FashionPoll.models import Fashionista, UserProfile, Order
from django.contrib.auth.models import User
from django.core import serializers
from datetime import datetime
import json
import datetime
# Create your views here.
def index(request):
	context_dict = {}
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
@login_required
def home(request):
	# TO show logged-in user details
	profile = UserProfile.objects.filter(user=request.user)[:1]
	# To show logged-in user's participation details / ask him to participate
	participation = Fashionista.objects.filter(user=request.user)[:1]
	# To generate 2 images at load/reload
	# Sort the fashionista in a random order
	# remove the logged-in user from the list
	fashionista_list = Fashionista.objects.all()
	flist1 = fashionista_list.exclude(user=request.user)

	# Now we need to escape from already-diplayed pairs.
	counter = flist1.count()
	if counter >= 2 :
		available = True
		total_pairs = (counter*(counter-1))/2
		pairs_liked = Order.objects.filter(liker = request.user)
		pairs_liked_counter = pairs_liked.count()
		if pairs_liked_counter < total_pairs :
			for element in flist1 :
				pairs_liked_having_element = pairs_liked.filter(liked = element.user) | pairs_liked.filter(unliked = element.user)
				if pairs_liked_having_element.count() < counter-1 :
					flag = False
					flist2 = flist1.exclude(user=element.user)
					for element2 in flist2 :
						if pairs_liked_having_element.filter(liked = element2.user).count() + pairs_liked_having_element.filter(unliked = element2.user).count()  == 0 :
							flag = True
							break

					if flag == True:
						break

			obj1 = element
			obj2 = element2
		else:
			available = False
			obj1 = False
			obj2 = False
	else:
		available = False
		obj1 = False
		obj2 = False
	context_dict = { 'uprofile' : profile, 
					 'uparticipation' : participation, 
					 'obj1' : obj1,
					 'obj2' : obj2,
					 'available' : available, }
	return render(request, 'FashionPoll/home.html', context_dict)

@login_required
def participate(request):
	participation = Fashionista.objects.filter(user=request.user)[:1]
	if participation.count() == 0 :
		registered = False
	else :
		registered = True

	if request.method == 'POST':
		form = FashionistaForm(request.POST, request.FILES)
		if form.is_valid():
			fashionista = form.save(commit=False)
			fashionista.user = request.user
			if 'fashionista_picture' in request.FILES:
				#print('yes')
				fashionista.fashionista_picture = request.FILES['fashionista_picture']

			fashionista.save()
			registered = True
		else:
			print('naruto')
			print(form.errors)
	else:
		form = FashionistaForm()

	return render(request,
		'FashionPoll/participate.html',
		{'registered': registered, 'form' : form} )

@login_required
def edit_profile(request):
	user1 = request.user
	profile = UserProfile.objects.get(user=request.user)
	edited = False
	if request.method == 'POST':
		form = UserProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			saved = form.save(commit = False)
			saved.user = request.user
			if 'profile_picture' in request.FILES:
				saved.profile_picture = request.FILES['profile_picture']
			saved.save()
			edited = True
		else:
			print('naruto')
			print(form.errors)
	else:
		form = UserProfileForm(instance=profile)
		
	context_dict = {'user' : user1, 'profile' : profile, 'edited' : edited, 'form' : form}
	return render(request, 'FashionPoll/edit_profile.html', context_dict)

@login_required
def like_picture(request):
	pic_id = None
	if request.method == 'GET':
		print("GOT it")
		liker = request.user
		liked_id = request.GET['liked']
		liked = User.objects.get(id = liked_id)
		unliked_id = request.GET['unliked']
		unliked = User.objects.get(id = unliked_id)
		pic_id = request.GET['pic_id1']
		instance = Order(liker = liker, liked = liked, unliked = unliked, created_at = datetime.now())
		instance.save()
	else:
		print("dipchik")
	likes = 0
	views = 0
	rating = 0
	if pic_id:
		pic = Fashionista.objects.get(id=int(pic_id))
		pic2 = Fashionista.objects.get(user=unliked)
		if pic:
			likes = pic.likes+1
			views = pic.views+1
			likes2 = pic2.likes
			views2 = pic2.views+1
			pic.likes = likes
			pic.views = views			
			pic2.views = views2			
			rating = pic.rating
			pic.rating = rating +((likes2*1.0)/(views2*1.0))
			rating = pic2.rating
			pic2.rating = rating -((likes*1.0)/(views*1.0))
			pic.save()
			pic2.save()


	# To generate 2 images at load/reload
	# Sort the fashionista in a random order
	# remove the logged-in user from the list
	fashionista_list = Fashionista.objects.all()
	flist1 = fashionista_list.exclude(user=request.user)

	# Now we need to escape from already-diplayed pairs.
	counter = flist1.count()
	if counter >= 2 :
		available = True
		total_pairs = (counter*(counter-1))/2
		pairs_liked = Order.objects.filter(liker = request.user)
		pairs_liked_counter = pairs_liked.count()
		if pairs_liked_counter < total_pairs :
			for element in flist1 :
				pairs_liked_having_element = pairs_liked.filter(liked = element.user) | pairs_liked.filter(unliked = element.user)
				if pairs_liked_having_element.count() < counter-1 :
					flag = False
					flist2 = flist1.exclude(user=element.user)
					for element2 in flist2 :
						if pairs_liked_having_element.filter(liked = element2.user).count() + pairs_liked_having_element.filter(unliked = element2.user).count()  == 0 :
							flag = True
							break

					if flag == True:
						break

			obj1 = element
			obj2 = element2
			serialized_obj = serializers.serialize('json',[obj1, obj2, ])
		else:
			available = False
			obj1 = False
			obj2 = False
			data = {}
			data['available'] = False
			serialized_obj = json.dumps(data)
	else:
		available = False
		obj1 = False
		obj2 = False
		data = {}
		data['available'] = False
		serialized_obj = json.dumps(data)

	print(serialized_obj)

	return HttpResponse(serialized_obj, content_type = "application/json")

def rank_list(request):
	flist = Fashionista.objects.order_by('-rating')
	context_dict = {'flist' : flist, }
	return render(request, 'FashionPoll/rank_list.html', context_dict)

def show_profile(request, username):
	user1 = User.objects.get(username = username)
	user1_profile = UserProfile.objects.get(user = user1)
	user1_fashionista = Fashionista.objects.get(user = user1)
	context_dict = {'user1' : user1, 'user1_profile' : user1_profile, 'user1_fashionista' : user1_fashionista, }
	return render(request, 'FashionPoll/show_profile.html',context_dict)

def graph(request,username):
	print("Graph is working")
	username1 = username
	user = User.objects.get(username = username1)
	obj1 = Order.objects.filter(liked = user).order_by('created_at')
	obj2 = obj1.values_list('created_at')
	data = []
	count = 1
	for element in obj2:
		x=[]
		a = element[0]
		print("a = ")
		print(a)
		a1 = datetime.datetime(a.year,a.month,a.day,a.hour,a.minute,a.second)
		print("a1 = ")
		print(a1)
		b = datetime.datetime(1970,1,1,0,0,0,)
		print("b = ")
		print(b)
		c = (a1-b).total_seconds()
		d = int(c*1000)
		x.append(d)
		x.append(count)
		count = count+1
		data.append(x)

	print(data)
	s = json.dumps(data)
	print(s)
	return HttpResponse(s, content_type = "application/json")

