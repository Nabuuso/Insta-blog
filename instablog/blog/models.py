from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import os

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,full_name,username,email,password,*args,**kwargs):
        if email is None:
            raise TypeError("Email field cannot be null")
        user = self.model(full_name=full_name,username=username,email=email,*args,**kwargs)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,password,*args,**kwargs):
        user = self.model(**kwargs)
        user.set_password(password)
        user.save()
        return user

class Profile(AbstractBaseUser,PermissionsMixin):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=255,unique=True)
    bio = models.TextField(null=True)
    profile_photo = models.ImageField(upload_to="images/profile",null=True)
    password = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','username','password']
    objects = UserManager()

    def __str__(self):
        return self.full_name
    class Meta:
        ordering = ['-created_date']
class Image(models.Model):
    image = models.ImageField(upload_to="images/blog",null=True)
    image_name = models.CharField(max_length=255)
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.image_name
    def save_image(self,*args,**kwargs):
        super().save(*args,**kwargs)
    def delete_image(self,pk):
        img = Image.objects.get(pk=pk)
        if len(img.image) > 0:
            os.remove(img.image.path)
        img.delete()
    def update_caption(self,*args,**kwargs):
        super().update(*args,**kwargs)
    
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Image,on_delete=models.CASCADE,related_name="image_comments")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="user_comments")
    def __str__(self):
        return self.comment
    class Meta:
        ordering = ['-created_date']
class Follower(models.Model):
    profiles = models.ManyToManyField(Profile, through="UserFollower")

class UserFollower(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    follower = models.ForeignKey(Follower,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile
    class Meta:
        ordering = ['-created_date']
class ProfileFollower(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="profiles_follower")
    user_follower = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="users_follower")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile
    class Meta:
        ordering = ['-created_date']

