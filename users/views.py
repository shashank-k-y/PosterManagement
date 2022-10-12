from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    template = loader.get_template('users/index.html')
    context = {
        'strings': ["hello", "world"],
        'greetings': "wellcome to home Page"
    }
    return HttpResponse(template.render(context, request))


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("successfully logged in!")

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context=context)

