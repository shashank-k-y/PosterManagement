from django.urls import path
from django.views.generic.base import RedirectView

from users import views

urlpatterns = [
    # path('home/', views.index, name='home'),
    path('signup/', views.register, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_request, name="logout"),
    path('staff/', RedirectView.as_view(url='/admin'), name='staff'),
    path('profile/', views.profile, name="profile")
]
