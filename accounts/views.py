from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileEditForm
from .models import Profile


def register_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        codename = request.POST.get("codename", "").strip()
        password = request.POST.get("password", "").strip()
        password2 = request.POST.get("password2", "").strip()

        if not username or not password or not codename:
            messages.error(request, "Fill in all fields.")
        elif password != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        elif Profile.objects.filter(codename=codename).exists():
            messages.error(request, "Codename already taken.")
        else:
            user = User.objects.create_user(username=username, password=password)
            Profile.objects.create(user=user, codename=codename, role="cadet")
            messages.success(request, "Account created. You can now log in.")
            return redirect("accounts:login")

    return render(request, "accounts/register.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect("accounts:profile")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("accounts:login")


@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, "accounts/profile.html", {"profile": profile})


@login_required
def profile_edit_view(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("accounts:profile")
    else:
        form = ProfileEditForm(instance=profile)

    return render(request, "accounts/profile_edit.html", {"form": form})


"""
ПРИКЛАД використання перевірки ролей в чужому app (наприклад "materials" або "events").
Цей файл не треба підключати — він лише демонструє, як інші учні
використовують accounts.permissions у своїх views.py.


from django.http import HttpResponse
from accounts.permissions import (
    is_cadet,
    is_instructor,
    is_admin_role,
    instructor_required,
    admin_required,
    role_required,
)


# 1) Звичайний курсант може ПЕРЕГЛЯДАТИ — доступно всім залогіненим
from django.contrib.auth.decorators import login_required

@login_required
def material_list(request):
    return HttpResponse("Список матеріалів — доступно всім курсантам.")


# 2) Інструктор (або admin) може СТВОРЮВАТИ матеріали / оголошення / події
@instructor_required
def create_announcement(request):
    return HttpResponse("Форма створення оголошення — тільки для інструкторів і адмінів.")


# 3) Тільки admin має повний доступ (наприклад видалення чужого контенту)
@admin_required
def delete_any_material(request):
    return HttpResponse("Видалення — тільки для admin.")


# 4) Кастомний набір ролей через role_required(...)
@role_required("instructor", "admin")
def create_event(request):
    return HttpResponse("Створення події — instructor + admin.")


# 5) Перевірка ролі прямо всередині view (без декоратора), коли логіка складніша
def event_detail(request, event_id):
    if is_admin_role(request.user):
        can_edit = True
    elif is_instructor(request.user):
        can_edit = True   # інструктор теж може редагувати свою подію
    else:
        can_edit = False  # звичайний cadet — лише перегляд

    return HttpResponse(f"Подія #{event_id}. Can edit: {can_edit}")
""