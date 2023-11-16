from django.urls import path
from .views import index, signup, custom_login, custom_logout
urlpatterns = [
    path('', index, name='index'),
    path('signup', signup, name='signup'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
]
