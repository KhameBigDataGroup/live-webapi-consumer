from django.urls import path

from bitcoinapi import views

urlpatterns = [
    path('bitcoin/get_status', views.get_status),
    path('bitcoin/get_latest_blocks', views.get_latest_blocks), 
    path('bitcoin/get_block/<int:height>/', views.get_block),
    path('bitcoin/get_transactions/<int:block_height>/', views.get_transactions),
    path('bitcoin/get_transactions/hash/<slug:hash>/', views.get_transaction_by_hash),
    path('bitcoin/get_transactions/address/<slug:address>/', views.get_transactions_address),
]
