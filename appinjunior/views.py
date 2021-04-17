from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import UserProfile 
from django.contrib.auth import authenticate, login, logout


def home(request):
	return render(request,'base.html')

def login_call(request):
	if request.method=='POST':
		url = '/login/'
		username=request.POST['username']
		password=request.POST['password']
		selUser = authenticate(username=username, password=password)
		if selUser:
			login(request, selUser)
			uObj = UserProfile.objects.get(user__username=request.user)
			if uObj.usertype == "student":
				return redirect('/student/home/')
			elif uObj.usertype == "teacher":
				return redirect('/teacher/home/')
		else:
			return HttpResponse('<script>alert("Incorrect username or password"); window.location="{}"</script>'.format(url))


	return render(request,'login.html')

def signup_call(request):
	if request.method=='POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		pname=request.POST['pname']
		dob=request.POST['dob']
		gen=request.POST['gen']
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		usertype=request.POST['usertype']
		mobile=request.POST['mobileno']
		laptop=request.POST['lap']
		address=request.POST['address']

		u = User(first_name=fname, last_name=lname, username=username, password=make_password(password), email=email)
		print(u)
		u.save()
		up = UserProfile(user=u,usertype=usertype,parentname=pname,dob=dob,gender=gen,mobile=mobile,laptop=laptop,address=address)
		print(up)
		up.save()
	return render(request,'signupage.html')



def logout_call(request):
	logout(request)
	return redirect('/')

def course(request):
	return render(request,'courses2.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')