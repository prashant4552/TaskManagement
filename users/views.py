from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):

    print("REQUEST METHOD:", request.method)

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        print("USERNAME:", username)
        print("PASSWORD:", password)

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print("AUTHENTICATED USER:", user)

        if user is not None:
            print("LOGIN SUCCESS")
            login(request, user)
            return redirect('dashboard')

        else:
            print("LOGIN FAILED")

            return render(
                request,
                'login.html',
                {
                    'error': 'Invalid username or password.'
                }
            )

    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')