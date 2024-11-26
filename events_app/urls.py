from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('event/', views.event, name='event'),
    path('participant/', views.participant, name='participant'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]
