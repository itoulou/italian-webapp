from django.shortcuts import render, reverse, redirect, HttpResponse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from authentication.forms import loginForm, registerForm

# Create your views here.
def login(request):
    if request.method == "POST":
        login_form = loginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Bentornato " + user.username)
                return redirect(reverse('home'))
            else:
                messages.error(request, "username or password is incorrect")
                return redirect(reverse('login'))
    else:
        login_form = loginForm()
    return render(request, 'login.html', {"login_form": login_form})
    
def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    if request.method == "POST":
        register_form = registerForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     email=request.POST['email'],
                                     password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Benvenuti " + user.username)
                return redirect(reverse('home'))
            else:
                messages.error(request, 'A problem occured, please try to register again')
              
           
    else:
        register_form = registerForm()
    return render(request, 'register.html', {"register_form": register_form})

@login_required    
def logout(request):
    """
    logout user
    """
    auth.logout(request)
    messages.success(request, "Grazie, Arrivederci")
    return redirect(reverse('login'))