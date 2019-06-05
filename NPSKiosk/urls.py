from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='NPS-Home'),
    path('search/', views.query, name='NPS-Search'),
    path('state/<str:stateCode>/', views.state, name='NPS-State'),
    path('dest/<str:parkCode>/', views.selected_destination, name='NPS-Destination'),
]