"""
URL configuration for DNICK_Lab4_Book_Store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import BookStore.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', BookStore.views.index, name="index"),
    path("books/<int:book_id>/", BookStore.views.book_detail, name="book_details"),
    path("index/", BookStore.views.index, name="index"),
    path("books/add/", BookStore.views.add_book, name="add_book")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)