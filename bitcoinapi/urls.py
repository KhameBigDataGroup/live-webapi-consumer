from django.urls import path

from bitcoinapi import views

urlpatterns = [
    path('bitcoin/get_status', views.get_status),
    path('bitcoin/get_latest_blocks', views.get_latest_blocks),
]
