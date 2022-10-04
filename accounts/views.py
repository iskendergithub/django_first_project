from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    contex = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, '\n', password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is None:
            contex = {"error": "Something go wrong ! Username or password is not correct !"}
        else:
            login(request, user)
            return redirect('/')
    return render(request, "accounts/login.html", contex)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login/')

    return render(request, "accounts/logout.html", {})
