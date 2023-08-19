"""MGN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/',Home,name='Home'),
    path('Registration/',Registration,name='Registration'),
    path('User_Login/',User_Login,name='User_Login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('transactions/',transactions,name='transactions'),
    path('History_display/',History_display,name="History_display"),
    path("Transactions_acc/",Transactions_acc,name="Transactions_acc"),
    path('forgot_password/',forgot_password,name='forgot_password'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
