from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def index(request):

    return render(request, 'accounts/index.html')


def about_us(request):

    return render(request, 'roaddog/about_us.html')


@csrf_exempt
def signup(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'accounts/signup.html', {'form': form})

    form = UserForm(request.POST)

    if form.is_valid():
        form.save()
        user_name = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user_name, password=raw_password)
        auth_login(request, user)
        return redirect('/')

    print(form.errors)

    return render(request, 'accounts/signup.html', {'form': form})


def mypage(request):

    return render(request, 'accounts/mypage.html')


def user_info(request):

    return render(request, 'accounts/user_info.html')


def survey_info(request):

    return render(request, 'accounts/survey_info.html')


def inquiry(request):

    return render(request, 'accounts/inquiry.html')
