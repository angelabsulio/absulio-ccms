from django.urls import path
from ccms import views

urlpatterns = [
    path('mission/', views.ccms_mission, name='ccms_mission'),
    path('vision/', views.ccms_vision, name='ccms_vision'),
    path('objectives/', views.ccms_objectives, name='ccms_objectives'),
]

