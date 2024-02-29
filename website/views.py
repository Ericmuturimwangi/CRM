from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def home(request):
    #check to asses if one is logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error")
            return redirect('home')
        
    else:
        return render(request, 'home.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, "You are logged out")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})
