"""bookSystem URL Configuration

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
from django.urls import path
import bookApp.views as bv
from bookApp.views import BookListView,BookDetailView,AddBookView,DelBookView,UpdateBookView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', bv.index),
    path('',BookListView.as_view(),name="bookList"),
    path('bookDetail/', BookDetailView.as_view(), name="BookDetail"),
    path('addBook/', AddBookView.as_view(), name="AddBook"),
    path('updateBook/', UpdateBookView.as_view(), name="UpdateBook"),
    path('delBook/', DelBookView.as_view(), name="DelBook")

]
