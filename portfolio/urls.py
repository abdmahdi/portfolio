from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
     path('send_email/', views.sendemail, name='send_email')
]
