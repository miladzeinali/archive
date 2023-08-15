from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
def loginview(request):
    if request.method == 'POST':
        form = request.POST
        if form:
            username = form['username']
            password = form['password']
            try:
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
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
        return render(request,'login.html')
