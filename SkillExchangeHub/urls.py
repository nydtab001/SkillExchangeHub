"""SkillExchangeHub1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, include
from skills import views
from users.views import register, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', views.skill, name='home'),
    path('accounts/', include('allauth.urls')),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('password_change/', PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
]
