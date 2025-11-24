from django.contrib import admin
from django.urls import path, include
from blogs.views import *


urlpatterns = [
    path('', post_list, name = 'post_list'),
    path('post/<int:pk>/', post_detail, name ='post_detail'),
    path('post/create/', post_create, name ='post_create'),
    path('post/<int:pk>/edit/', post_update, name ='post_update'),
    path('post/<int:pk>/delete/', post_delete, name ='post_delete'),
    path('login/', login_view, name='login'),
    path('register/', registration_view, name ='register'),
    path('logout/', logout_view, name ='logout' )
]

