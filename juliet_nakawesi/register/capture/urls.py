from django.urls import path
from capture import views

urlpatterns = [
    path('',views.register,name='base.html'),
    path('register/',views.register,name='register'),
]