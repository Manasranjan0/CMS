from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def homepage(request):
    return render(request,'index.html')
def addlogin(request):
    return render(request,'loginpage/loginPage.html')
def StudentSignUp(request):
    return render(request,'signuppage/studentsignuppage.html')