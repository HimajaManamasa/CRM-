from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import contact,post
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.

from .forms import Text,postForm


def home(request):
    return render(request,'index.html')

def number(request):
    return render(request,'contact.html')

def books(request):
    return render(request,'contact.html')

def get_name(request):

    if request.method == 'POST':
        form = Text(request.POST)
        if form.is_valid():
            print (form.cleaned_data['Name'])
            contact.objects.create(name = form.cleaned_data['Name'])
            return HttpResponseRedirect('/contact')
    else:
        form = Text()

    return render(request,'name.html',{'form':form})

def names(request):
    names = contact.objects.all()
    return render(request,'names.html',{'names':names})   

def edit_name(request,edit_name):
    name_obj = contact.objects.get(id=edit_name) 
    if request.method =='POST':
        form = Text(request.POST)
        if form.is_valid():
            name_obj.name = form.cleaned_data['Name']
            name_obj.save()
            return HttpResponse('/home')
    else:
        form = Text()
    return render(request,'edit.html',{'form':form,'name_obj':name_obj})   

def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request,user)
            return HttpResponse('home')
        else:
            return render(request,'signup.html',{'form': form})
    else:
        form = UserCreationForm()
        return render(request,'signup.html',{'form': form})

def login(request):
    if request.method =='POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request,user)
            return HttpResponse('home')

        else:
            print(form.errors)
            return render(request,'login.html',{'form':form})
    else:
        form = AuthenticationForm()      
        return render(request,'login.html',{'form':form})

def create_post(request):
    if request.method == 'POST':
       print(request.user)
       form = postForm(request.POST)
       if form.is_valid():
            post = form.save(commit=False)
            print(form.cleaned_data['title'])
            print(form.cleaned_data['text'])
            post.author = request.user
            post.published_date = timezone.now()
            form.save()
            return redirect('allnames')
    else:
        form = postForm()
        return render(request,'post.html',{'form':form})

def all_post(request):
    posts = post.objects.all()
    return render(request,'all_post.html',{'post':posts})




