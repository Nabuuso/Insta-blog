from django.shortcuts import render,redirect
from django.views import View
import json
from django.http import JsonResponse
from . models import *
from django.core.mail import EmailMessage
from django.contrib import auth
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request,'authentication/login.html')
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        if email and password:
            user = auth.authenticate(email=email,password=password)
            if user:
                auth.login(request,user)
                return redirect('/dashboard')
            else:
                messages.error(request,'Invalid login')
                return render(request,'authentication/login.html')
        messages.error(request,'Invalid login credentials')
        return render(request,'authentication/login.html')
        # return JsonResponse({"error":"Invalid credentials!"},status=400)
class LogoutView(View):
    def post(self,request):
        auth.logout(request)
        messages.success(request,"You have successfully logged out")
        return redirect('login')
####REGISTER VIEW
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
                email.send(fail_silently=True)
                return JsonResponse({"message":"Account created successfully","status":201},status=201)
            else:
                return JsonResponse({"error":"Username already taken","status":400},status=400)
        else:
            return JsonResponse({"error":"Email already taken","status":400},status=400)
###CLASS DASHBOARD VIEW
class DashboardView(View):
    def get(self,request):
        return render(request,'dashboard/index.html')
#######BLOG IMAGES
class BlogImageView(View):
    def post(self,request):
        img = request.FILES.get("image")
        image_name = request.POST['image_name']
        image_caption = request.POST['image_caption']
        profile = request.POST['profile']
        fss = FileSystemStorage()
        filename = fss.save(img.name,img)
        url = fss.url(filename)
        img_object = Image()
        img_object.image = url
        img_object.image_name = image_name
        img_object.image_caption = image_caption
        p = Profile.objects.get(pk=profile)
        img_object.profile = p
        img_object.save_image()
        # Image.save_image(image=url,image_name=image_name,image_caption=image_caption,profile=profile)
        return JsonResponse({"success":"Image uploaded successfully","status":201},status=201)