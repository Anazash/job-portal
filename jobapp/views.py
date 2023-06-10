from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def products(request):
    return render(request,'products.html')

def resources(request):
    return render(request,'resources.html')

def helpcenter(request):
    return render(request,'helpcenter.html')

def findjobs(request):
    return render(request,'findjobs.html')

def postjobs(request):
    return render(request,'postjobs.html')

def showjob(request):
    return render(request,'showjob.html')

def messages(request):
    return render(request,'messages.html')

def profile(request):
    return render(request,'profile.html')

def seeprofile(request):
    return render(request,'seeprofile.html')