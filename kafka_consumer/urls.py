from django.contrib import admin
from django.urls import path

from kafka_consumer import views

urlpatterns = [
    path('latest_block', views.latest_block),
]
