from django.shortcuts import render
from Auth.forms import UserInfoForm
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from Auth.models import UserInfo
import jwt
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

salt = '5eC437/\9&*'


def index(request):
    return render(request, 'index.html')


def register(request):
    registered = False
    status_code = 200
    if request.method == 'POST':
        profile_form = UserInfoForm(data=request.POST)
        # print(profile_form)
        if profile_form.is_valid():
            hashPassword = make_password(
                profile_form.cleaned_data['password'], salt)
            profile = profile_form.save(commit=False)
            profile.password = hashPassword
            profile.save()
            status_code = 201
            registered = True
        else:
            # print(profile_form.errors)
            status_code = 203
    else:
        profile_form = UserInfoForm()
    temp = loader.get_template('registration.html')
    tempStuff = {'profile_form': profile_form, 'registered': registered}
    return HttpResponse(temp.render(tempStuff, request), content_type='text/html', status=status_code)


@csrf_exempt
def oauth(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'), salt)
        try:
            user = UserInfo.objects.get(email=email, password=password)

        except UserInfo.DoesNotExist:
            # print("Someone tried to login and failed.")
            print("They used email: {} and password: {}".format(email, password))
            return HttpResponse("Invalid login details given", status=203)

        if user:
            payload = {
                'id': user.id,
                'email': user.email,
            }
            jwt_token = {'token': jwt.encode(
                payload, "SECRET_KEY").decode('utf-8')}
            return HttpResponse(json.dumps(jwt_token), status=200, content_type="application/json")
        else:
            return HttpResponse(json.dumps({'Error': "Invalid credentials"}), status=400, content_type="application/json")
    else:
        return render(request, 'login.html', {})


def home(request):
    auth = request.headers.get('Authorization')
    # print('header:',request.headers))
    if not auth:
        return HttpResponse({'Error': "Not Authenticated"}, status="501")

    payload = jwt.decode(auth, "SECRET_KEY")
    email = payload['email']
    userid = payload['id']
    # msg = {'Error': "Token mismatch", 'status': "401"}
    try:
        user = UserInfo.objects.get(email=email, id=userid)

    except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
        return HttpResponse({'Error': "Token is invalid"}, status="403")
    except UserInfo.DoesNotExist:
        return HttpResponse({'Error': "Internal server error"}, status="500")

    return HttpResponse(json.dumps({"name": user.name}), content_type="application/json")
