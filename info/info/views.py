from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt


from . import forms


def logout_user(request):
    logout(request)
    return redirect('login')

@csrf_exempt
def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        user = authenticate(
                username=request.POST['username'],
                password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponse('ログインしました')
    return render(request, 'registration/login.html', context={'form': form, 'message': 'ログインしていません'})

def abc(request):
    return HttpResponse('ログインに成功しました')