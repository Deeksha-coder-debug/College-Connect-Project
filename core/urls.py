from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
