from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('materials/', views.materials_view, name='materials'),
    path('attendance/', views.attendance_view, name='attendance'),
    path('events/', views.events_view, name='events'),
    path('announcements/', views.announcements, name='announcements'),
]
