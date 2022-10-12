from django.urls import path

from users import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('signup/', views.register, name='signup')
]