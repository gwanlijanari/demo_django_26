import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from requests.models import Tutorial
from courses.models import Course

User = get_user_model()

@pytest.mark.positive
@pytest.mark.django_db
def test_enroll_in_course(client):
    user = User.objects.create_user(username='student1', password='password123')
    student = user.student
    course = Course.objects.create(code='A1')
    
    client.login(username='student1', password='password123')
    
    url = reverse('requests:create')
    data = {
        'title': 'тест курс',
        'course': course.id,
        'payment_method': Tutorial.PaymentChoices.cash,
    }
    response = client.post(url, data)
    
    assert response.status_code == 302
    assert Tutorial.objects.filter(student=student, course=course).exists()
    
    tutorial = Tutorial.objects.get(student=student, course=course)
    assert tutorial.status == Tutorial.StatusChoice.new