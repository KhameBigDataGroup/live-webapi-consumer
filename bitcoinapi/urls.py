from django.urls import path

from bitcoinapi import views

urlpatterns = [
    path('bitcoin/get_status', views.get_status),
    path('bitcoin/get_latest_blocks', views.get_latest_blocks), 
    path('bitcoin/get_blocks_from/<slug:hash>/', views.get_blocks_from),
    path('bitcoin/get_block/<slug:hash>/', views.get_block),
    path('bitcoin/get_transactions/<slug:block_hash>/', views.get_transactions),
    path('bitcoin/get_transaction/<slug:hash>/', views.get_transaction_by_hash),
    path('bitcoin/get_charts', views.get_charts),
]
