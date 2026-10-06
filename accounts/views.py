from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, "home.html")


def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.role == "HOSPITAL":
                return redirect("hospital_dashboard")

            elif user.role == "ADMIN":
                return redirect("admin_dashboard")

            else:
                return redirect("search")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(
        request,
        "accounts/login.html"
    )


def register(request):

    if request.method == "POST":

        from .models import User

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            phone=phone,
            role="USER"
        )

        login(request, user)

        return redirect("search")

    return render(
        request,
        "accounts/register.html"
    )


def user_logout(request):

    logout(request)

    return redirect("home")