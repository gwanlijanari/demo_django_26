from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TutorialForm, ReviewForm
from .models import Tutorial, Review
from courses.models import Course

@login_required
def create_tutorial(request):
    course_id = request.GET.get('course')
    course = Course.objects.get(id=course_id) if course_id else None
    
    if request.method == 'POST':
        form = TutorialForm(request.POST)
        if form.is_valid():
            tutorial = form.save(commit=False)
            tutorial.student = request.user.student
            tutorial.save()
            messages.success(request, 'Заявка отправлена')
            return redirect('accounts:profile')
    else:
        initial = {}
        if course:
            initial['course'] = course
        form = TutorialForm(initial=initial)
    
    return render(request, 'requests/create.html', {
        'form': form,
        'course': course,
    })

@login_required
def create_review(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    
    if tutorial.status != 'обучение завершено':
        messages.error(request, 'Отзыв можно оставить только на завершённый курс')
        return redirect('accounts:profile')
    
    existing = Review.objects.filter(student=request.user.student, tutorial=tutorial).first()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=existing)
        if form.is_valid():
            review = form.save(commit=False)
            review.student = request.user.student
            review.tutorial = tutorial
            review.save()
            messages.success(request, 'Отзыв сохранён')
            return redirect('accounts:profile')
    else:
        form = ReviewForm(instance=existing)
    
    return render(request, 'requests/review.html', {
        'form': form,
        'tutorial': tutorial,
        'existing_review': existing,
    })