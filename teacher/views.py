from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'dashboard.html',{'name':request.user.first_name})
