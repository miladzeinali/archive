from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
def loginview(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.user)
        form = request.POST
        print(form)
        if form:
            username = form['username']
            password = form['password']
            print(password)
            print(username)
            try:
                user = authenticate(request,username=username,password=password)
                print(user)
                if user is not None:
                    print('21')
                    login(request,user)
                    print('23')
                    messages.success(request, 'Welcome, YOU ARE LOGIN, ENJOY IT!', 'success')
                    print('25')
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
