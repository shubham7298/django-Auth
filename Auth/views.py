from django.shortcuts import render
from Auth.forms import UserInfoForm

def index(request):
    return render(request,'index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        profile_form = UserInfoForm(data=request.POST)
        print(profile_form)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
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
    pass