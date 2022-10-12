from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from users import forms


# Create your views here.

@login_required(login_url='accounts/login')
def index(request):
    template = loader.get_template('users/index.html')
    context = {
        'strings': ["hello", "world"],
        'greetings': "wellcome to home Page"
    }
    return HttpResponse(template.render(context, request))


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = forms.CreateUserForm()

    if request.method == "POST":
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request=request,
                message=f"account created successfully for {username} !"
            )
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context=context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = forms.LoginForm()
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data.get("username")
            password = data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect('home')
            else:
                messages.info(
                    request, "Username or passsword is incorrect!"
                )

    context = {
        "form": form
    }
    return render(request, 'users/login_page.html', context=context)


def logout_request(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = forms.UpdateProfileForm(
            request.POST, instance=request.user
        )
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
        else:
            messages.error(request, "something wrong with username or email")
    else:
        user_form = forms.UpdateProfileForm(instance=request.user)

    return render(request, 'users/profile.html', {'form': user_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')
