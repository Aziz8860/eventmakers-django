from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('events/create/', views.CreateEventView.as_view(), name='create_event'),
    path('events/<str:event_id>/', views.EventDetailView.as_view(), name='event_detail'),
]
