"""core URL Configuration

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
from rest_framework.routers import DefaultRouter

from library.views import LibraryViewSet, BookViewSet, LibraryBookViewSet, ActivityList, ActivityDetail, \
    UserLibraryViewSet

router = DefaultRouter()
router.register(r'libraries', LibraryViewSet)
router.register(r'books', BookViewSet)
router.register(r'user_library', UserLibraryViewSet)
router.register(r'library_books', LibraryBookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('LibraryActivity/', ActivityList.as_view(), name='activities'),
    path('LibraryActivity/<int:pk>/', ActivityDetail.as_view(), name='activity'),
]

test = 'asas'