from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.template import Context
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.urls import reverse

from user_manager.forms import LoginForm, RegisterForm


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(
            reverse('post_service:post_list'))  # first page after login.   # in explorer, what I want does work well

    template = get_template('login_form.html')
    # context = Context({'login_form': LoginForm()})
    context = Context({'form': LoginForm()})  #change name to share django default login form
    context.update(csrf(request))

    return HttpResponse(template.render(context))


def login_validate(request):
    login_form_date = LoginForm(request.POST)

    if login_form_date.is_valid():

        user = auth.authenticate(username=login_form_date.cleaned_data['id'],
                                 password=login_form_date.cleaned_data['password'])

        if user is not None:
            # if user.is_active:
            auth.login(request, user)
            request.session['member_id'] = user.username
            return HttpResponseRedirect(reverse("post_service:post_list"))
            # else:
            #     print HttpResponse("Is not active")
        else:
            return HttpResponse("User doen't exist or password is wrong")
    else:
        return HttpResponse('Login form is not valid')

    return HttpResponse('Unknown errors happen')


def logout(request):
    try:
        del request.session['member_id']
        auth.logout(request)
    except KeyError:
        pass
    return HttpResponse("You're logged out.")


def signup(request):
    if request.method == "POST":
        userform = RegisterForm(request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect(reverse("user_manager:signup_ok"))

    elif request.method == "GET":
        userform = RegisterForm()

    return render(request, "signup.html", {"userform": userform})
