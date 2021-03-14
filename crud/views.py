from django import forms
from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from .models import user
from .forms import LoginForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



# Create your views here.
def index(request): 
    res = user.objects.all()
    p = Paginator(res,3)
    page_num = request.GET.get('page',1)

    try:
      page = p.page(page_num)
    except EmptyPage:
      page = p.page(1)
    except PageNotAnInteger:
      page = p.page(1)   
      
    form = LoginForm()
    return render(request,'crud/index.html',{'res':page,'form':form})
 



def insert(request):
 if request.method== "POST":
  fm = LoginForm(request.POST)
  if fm.is_valid():
   name= fm.cleaned_data['name']
   email = fm.cleaned_data['email']
   password = fm.cleaned_data['password']
   reg = user(name=name,email=email,password=password)
   reg.save()
   fm = LoginForm()
   return redirect('index')
 else:
  return redirect('index') 


def delete(request,id):
      data = user.objects.get(pk=id)
      data.delete()
      return redirect('index')


def edit(request,id):
    if request.method=="POST":
      # return HttpResponse(id)
      pi = user.objects.get(pk=id)
      form = LoginForm(request.POST,instance=pi)
      if form.is_valid():
            form.save()
            return redirect('index')
    else:
        pi = user.objects.get(pk=id)
        form = LoginForm(instance=pi)      
    return render(request,'crud/updateForm.html',{'id':id,'form':form})

