"""
smtp_app  App urls
"""
from django.urls import path
from . import views

urlpatterns = [

    path('sender', views.Sender.as_view(), name="sender"),
]
