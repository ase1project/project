from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('signup/', views.signup, name = 'signup'),
    path('fgg/', views.forgotpassword, name = 'forgotpassword'),
]
