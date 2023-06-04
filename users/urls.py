from django.urls import path
from . import views
urlpatterns = [
    path('authorisation/', views.authorisation_view),
    path('registration/', views.registration_view),
]