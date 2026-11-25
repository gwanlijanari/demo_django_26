from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from requests.models import Tutorial, Review


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "регистрация прошла успешно")
            return redirect("accounts:login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile_view(request):
    tutorials = Tutorial.objects.filter(
        student=request.user.student,
    )
    reviews = Review.objects.filter(student=request.user.student)
    return render(
        request, "accounts/profile.html", {"tutorials": tutorials, "reviews": reviews}
    )
