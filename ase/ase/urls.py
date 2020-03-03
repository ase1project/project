from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from userapp import views as user_views


urlpatterns = [
    path('', include('homepage.urls')),
    path('dashboard/', include('userapp.urls')),
    path('admin/', admin.site.urls),
    path('signin/', auth_views.LoginView.as_view(template_name='homepage/signin.html'), name = 'signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='homepage/home.html'), name = 'logout'),
]
