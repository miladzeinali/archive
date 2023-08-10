from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

def login(request):
    if request.method == 'POST':
        form = request.POST
        if form:
            username = form['username']
            password = form['passweord']
            try:
                user = User.objects.get(username=username, password=password)
                if user:
                    login(request, user)
                    messages.success(request, 'Welcome, YOU ARE LOGIN, ENJOY IT!', 'success')
                    return redirect('coding:category')
                else:
                    messages.error(request, 'Error in Django Auth, CALL YOR PROVIDER! (code:20acc/vi)',
                                   'error')
                    return redirect('account:login')
            except:
                messages.error(request, 'Error in Django Auth, CALL YOR PROVIDER! (code:23acc/vi)',
                               'error')
                return redirect('account:login')
        else:
            messages.error(request, 'Error in Django Auth, CALL YOR PROVIDER! (code:28acc/vi)',
                           'error')
            return redirect('account:login')
    else:
        return render(request, 'login.html')
