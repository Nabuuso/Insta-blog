from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from . models import *
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
                # profile.set_password(password)
                profile.save()
                return JsonResponse({"message":"Account created successfully"})
            else:
                return JsonResponse({"error":"Username already taken"})
        else:
            return JsonResponse({"error":"Email already taken"})
# def index(request):
#     return render(request,'authentication/login.html')