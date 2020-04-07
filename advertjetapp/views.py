from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login,authenticate,logout
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

def create_inactive_user(username, email, password,first_name,last_name):
    new_user = User.objects.create_user(username, email, password)
    new_user.is_active = False
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.save()
    return 0

def createnewposts(request):
    if request.method == 'POST' and request.FILES['picture']:        
        title = request.POST.get('title', None)
        body = request.POST.get('body', None)
        picture = request.FILES['picture']
        fs = FileSystemStorage()
        filename = fs.save(picture.name, picture)
        file_url = fs.url(filename)
        PostObj=Post()
        PostObj.Title=title
        PostObj.Body=body
        PostObj.Cover=filename
        PostObj.save()
        return HttpResponseRedirect(reverse("services"))

def evans43(request):
    template_name="evans43.html"
    context={}
    return render(request,template_name,context)

def index(request):
    template_name="index.html"
    Post_list=Post.objects.all()
    context={'Post_list':Post_list}
    return render(request,template_name,context)
    
def services(request):
    template_name="services.html"
    context={}
    return render(request,template_name,context)
    
def about(request):
    template_name="about.html"
    context={}
    return render(request,template_name,context)

def contact(request):
    template_name="contact.html"
    context={}
    return render(request,template_name,context)

def subscribe(request):
    template_name="login.html"
    context={}
    return render(request,template_name,context)
    
def register(request):
    template_name="register.html"
    context={}
    return render(request,template_name,context)
    
def validatemylogin(request):
    name = request.POST.get('name', None)
    email = request.POST.get('email', None)
    data = {}    
    data['email_exists']=False    
    if EmailAlert.objects.filter(Email=email).exists():
        data['email_exists']=True
    if not data['email_exists']:
            EmailAlertObj = EmailAlert()
            EmailAlertObj.Name=name
            EmailAlertObj.Email=email
            EmailAlertObj.save()
            data['is_saved'] = True
    return JsonResponse(data)