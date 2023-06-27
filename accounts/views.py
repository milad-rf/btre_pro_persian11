from distutils.command.build_scripts import first_line_re
import imp
from pyexpat.errors import messages
from contacts.models import contacts
from django.shortcuts import render, redirect
from django.contrib import messages,  auth
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
      username = request.POST['username']   
      password = request.POST['password']   

      user = auth.authenticate(username=username, password=password)

      if user is not None:
            auth.login(request, user)
            messages.success(request, 'U R now logged in')
            return redirect('dashboard')
      else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request , 'U R logged out')
        return redirect('index')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'that username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'that email is being used')
                    return redirect('register')
                else:
                   user =  User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
                #    auth.login(request, user)
                #    messages.success(request, 'U R NOW LOGED IN')
                #    return redirect('index')
                user.save()
                messages.success(request, 'U R NOW registered & can log in')
                return redirect('login')
        else:
            messages.error(request, 'passwords do not match')
            return redirect('register')
    else:
        return render (request, 'accounts/register.html')

def dashboard(request):
    user_contacts = contacts.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts' : user_contacts,
    }
    if request.method == 'POST':
         return   
    else:
        return render(request, 'accounts/dashboard.html', context)
