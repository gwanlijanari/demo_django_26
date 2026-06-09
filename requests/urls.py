from django.urls import path
from . import views

app_name = 'requests'

urlpatterns = [
    path('create/', views.create_tutorial, name='create'),
    path('review/<int:tutorial_id>/', views.create_review, name='review'),
]