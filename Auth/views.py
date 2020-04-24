from django.shortcuts import render
from Auth.forms import UserInfoForm
from django.contrib.auth.hashers import make_password
from Auth.models import UserInfo
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

salt = '5eC437/\9&*'
def index(request):
    return render(request,'index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        profile_form = UserInfoForm(data=request.POST)
        # print(profile_form)
        if profile_form.is_valid():
            hashPassword = make_password(profile_form.cleaned_data['password'],salt)            
            profile = profile_form.save(commit=False)            
            profile.password = hashPassword
            profile.save()
            registered = True
        else:
            print(profile_form.errors)
    else:
        profile_form = UserInfoForm()
    return render(request,'registration.html',
                          {'profile_form':profile_form,
                           'registered':registered})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'),salt)
        try:
            print(UserInfo.objects.get(email=email,password=password))
            return HttpResponseRedirect(reverse('index'))

        except:
            print("Someone tried to login and failed.")
            print("They used email: {} and password: {}".format(email,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})