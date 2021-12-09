from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from . models import *
from django.core.mail import EmailMessage
# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request,'authentication/login.html')
class RegisterView(View):
    def get(self,request):
        return render(request,'authentication/register.html')
    def post(self,request):
        username = request.POST['username']
        email = request.POST['email']
        full_name = request.POST['full_name']
        password = request.POST['password']
        if not Profile.objects.filter(username=username).exists():
            if not Profile.objects.filter(email=email).exists():
                profile = Profile.objects.create_user(username=username,email=email,password=password,full_name=full_name)
                print(profile)
                # profile.set_password(password)
                profile.save()
                email = EmailMessage(
                    'InstaBlog Account',
                    'InstaBlog account created successfully',
                    'muuyiandrew2015@gmail.com',
                    [email]
                )
                email.send(fail_silently=False)
                return JsonResponse({"message":"Account created successfully","status":201},status=201)
            else:
                return JsonResponse({"error":"Username already taken","status":400},status=400)
        else:
            return JsonResponse({"error":"Email already taken","status":400},status=400)
# def index(request):
#     return render(request,'authentication/login.html')