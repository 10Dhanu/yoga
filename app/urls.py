from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    #path('book/<int:class_id>/', views.book_class, name='book_class'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('book/', views.book_class, name='book_class'),

]
