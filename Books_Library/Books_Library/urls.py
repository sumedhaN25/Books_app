"""
URL configuration for Books_Library project.

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
from book1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name="index_page"),
    path('show_books', views.show_books, name="show_books"),
    path('add_books', views.add_books, name='add_books'),
    path('update_book', views.update_book, name="update_book"),
    path('delete_book/', views.delete_book, name='delete_book'),

    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),

]
