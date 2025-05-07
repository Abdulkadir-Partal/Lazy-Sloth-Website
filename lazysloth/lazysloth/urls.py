"""
URL configuration for lazysloth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from productivity import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('concentrate_now/',views.concentrate_now, name='concentrate_now'),
    path('my_goals/',views.my_goals, name='my_goals'),
    path('save_time_data/', views.save_time_data, name='save_time_data'),
    path('report/', views.report_view, name='report'),
    path('users/', views.user_list, name='user_list'),
]


