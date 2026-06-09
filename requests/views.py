from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TutorialForm, ReviewForm
from .models import Tutorial

@login_required
def create_tutorial(request):
    if request.method == 'POST':
        form = TutorialForm(request.POST)
        if form.is_valid():
            tutorial = form.save(commit=False)
            tutorial.student = request.user.student
            tutorial.save()
            messages.success(request, 'Заявка отправлена')
            return redirect('accounts:profile')
    else:
        form = TutorialForm()
    return render(request, 'requests/create.html', {'form': form})


@login_required
def create_review(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    if tutorial.status != 'done':
        messages.error(request, 'отзыв можно ставить только завершенным курсам')
        return redirect('accounts:profile')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.student = request.user.student
            review.tutorial = tutorial
            review.save()
            messages.success(request, 'Отзыв оставлен')
            return redirect('accounts:profile')
    else:
        form = ReviewForm()
    return render(request, 'requests/review.html', {'form': form, 'tutorial': tutorial})