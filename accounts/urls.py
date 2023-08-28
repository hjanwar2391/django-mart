from django.urls import  path
from . import views
urlpatterns = [
    path('register/', views.registrar, name='register'),
    path('profile/', views.profile , name='profile'),
    path('login/', views.user_login, name='login'),
]
