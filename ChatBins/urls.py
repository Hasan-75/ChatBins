"""ChatBins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path, include
from chatapp.views import IndexView, SignupView, Messanger, active_users_list

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', IndexView.as_view(), name = 'index'),
    re_path(r'^', include('django.contrib.auth.urls')),
    re_path(r'^signup/$', SignupView.as_view(), name = 'signup'),
    re_path(r'^messages/$', Messanger.as_view(), name = 'messenger'),
    re_path(r'^messages/active_users$', active_users_list, name = 'active_users')

]
