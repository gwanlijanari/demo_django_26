import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from requests.models import Tutorial, Review
from courses.models import Course

User = get_user_model()

@pytest.mark.negative
@pytest.mark.django_db
def test_review_only_for_done_tutorial(client):
    user = User.objects.create_user(username='student1', password='password123')
    student = user.student
    course = Course.objects.create(code='A1')
    
    active_tutorial = Tutorial.objects.create(
        title='Активная', course=course, student=student,
        status=Tutorial.StatusChoice.active
    )
    
    client.login(username='student1', password='password123')
    url = reverse('requests:review', args=[active_tutorial.id])
    response = client.post(url, {'value': 'Круто!'})
    
    assert not Review.objects.filter(tutorial=active_tutorial).exists()
    
@pytest.mark.positive
@pytest.mark.django_db
def test_review_for_done_tutorial(client):
    user = User.objects.create_user(username='student2', password='password123')
    student = user.student
    course = Course.objects.create(code='A2')
    
    done_tutorial = Tutorial.objects.create(
        title='Завершенная', course=course, student=student,
        status=Tutorial.StatusChoice.done
    )
    
    client.login(username='student2', password='password123')
    url = reverse('requests:review', args=[done_tutorial.id])
    response = client.post(url, {'value': 'Круто!'})
    
    assert Review.objects.filter(tutorial=done_tutorial).exists()