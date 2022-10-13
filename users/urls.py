from django.urls import path
from django.views.generic.base import RedirectView

from users import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_request, name="logout"),
    path('staff/', RedirectView.as_view(url='/admin'), name='staff'),
    path('profile/', views.profile, name="profile"),
    path(
        'password-change/', views.ChangePasswordView.as_view(), 
        name='password_change'
    ),
    # path('index/', RedirectView.as_view(url='home'), name='index'),
]
