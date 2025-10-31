"""
URL configuration for IcentFramework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
""" 定义Icent的URL模式"""

from django.urls import path
from . import views

app_name = 'Icent'
urlpatterns = [
    #主页
    path('', views.index,name='index'),
    # 显示所有用户组的页面
    path('usergroups/', views.usergroups, name='usergroups'),
]
