
from django.views import View

from onlineapp.models import *
from django.http import *
from django.shortcuts import *

from onlineapp.models import *
from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from onlineapp.forms import *
from django.urls import *
from onlineapp.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


class SignUpView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('onlineapp/college')
        form = SignUpForm
        return render(
            request,
            'onlineapp/signup.html',
            {
                'form' : form,
            }
        )
    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user = authenticate(
                request,
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']

            )
            if user is not None:
                login(request, user)
                return redirect('onlineapp:college_html')
            else:
                messages.error(request,'invalid credentials')

            # return render(
            #     request,
            #     'onlineapp/signup.html',
            #     {
            #         'form': form,
            #     }
            # )
                return render("onlineapp:signup")

class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('onlineapp:college_html')
        form = LoginForm
        return render(
            request,
            'onlineapp/login.html',
            {
                'form' : form,
            }
        )
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']

            )
            if user is not None:
                login(request, user)
                return redirect('onlineapp:college_html')
            else:
                messages.error(request,'invalid credentials')

            return render(
                request,
                'onlineapp/login.html',
                {
                    'form': form,
                }
            )


def logout_user(request):
    logout(request)
    return redirect('onlineapp:login')