"""config URL Configuration

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
from django.urls import path, include

from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('dashboard1', views.dashboard1, name='dashboard1'),
    path('dashboard2', views.dashboard2, name='dashboard2'),
    path('dashboard3', views.dashboard3, name='dashboard3'),
    path('tabledata', views.tabledata, name='tabledata'),
    path('chart1', views.chart1, name='chart1'),
    path('chart2', views.chart2, name='chart2'),
]
