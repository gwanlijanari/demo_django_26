from django.shortcuts import render
from courses.models import Course
from requests.models import Review
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    courses = Course.objects.select_related('transport').all()
    reviews = Review.objects.select_related('tutorial__course').order_by('-id')[:5]
    return render(request, 'index.html', {
        'courses': courses,
        'reviews': reviews,
    })