from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm

# Create your views here.
def login_view(request):
    if request.method == 'GET':

        login_form = LoginForm()

        return render(request, 'login.html', {'login_form': login_form, 'show_logout': False})

    elif request.method == 'POST':
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, "Problem completing the form")
            return render(request, 'login.html', {'login_form': login_form, 'show_logout': False})

def logout_view(request):
    if request.method == 'POST':
        logout(request)

        return redirect('login_view')