from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView
from .views import generate_and_verify_zkproof


urlpatterns = [
    path('generate_and_verify_zkproof/', generate_and_verify_zkproof, name='generate_and_verify_zkproof'),
]