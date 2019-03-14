from django.urls import include, path
from landing import views

urlpatterns = [
    path('', views.landing, name='landing'),
]
