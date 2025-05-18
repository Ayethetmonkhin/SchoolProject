"""
URL configuration for school project.

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
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from schoolapp1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',indexView,  name='indexView'),
    path('course/',courseView, name='courseView'),
    path('train/',trainerView, name='trainerView'),
    path('about/',aboutView, name='aboutView'),
    path('contact/',contactView, name='contactView'),
    path('event/',eventView,name='eventView'),
    path('addc/', addCourse, name='addCourse'),
    path('addt/',addTeacher,name ='addTeacher'),
    path('updatec/<int:pk>/', updateCourse,name='updateCourse'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

