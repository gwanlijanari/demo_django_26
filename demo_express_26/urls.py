from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='accounts:login'), name='index'),
    path("", views.index, name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('requests/', include('requests.urls')),
]