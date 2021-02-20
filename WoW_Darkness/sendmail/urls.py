from .views import *
from django.urls import path

urlpatterns = [
    path('', index),
    # path('contact/', contact_view, name='contact'),
    # path('success/', success_view, name='success'),
]