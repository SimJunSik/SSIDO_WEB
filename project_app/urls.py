"""ssido URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('', views.index),
    path('cc_test/', views.cc_test),
    url(r'^joinClass/.+$',views.joinClass),
    path('inputClass/', views.inputClass),
    #path('pdf_upload/', views.pdf_upload),
    #path('pdf/', views.pdf),

    path('updateChat/', views.updateChat),
    path('sendChat/', views.sendChat),
    path('ddabong/', views.ddabong),
    path('delete_msg/', views.delete_msg),
    path('create_class/', views.create_class),
    path('check_class/', views.check_class),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)