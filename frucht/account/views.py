from django.shortcuts import render

# Create your views here.
def account_login(request):
    return render(request, 'account/login.html', {
        "email": request.GET.get('email', 0),
        "password": request.GET.get('password', 0),
    })
