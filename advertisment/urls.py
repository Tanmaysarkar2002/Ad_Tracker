from django.urls import path
from . import views

urlpatterns = [
    path('advertisers/', views.AdvertiserViewSet.as_view({'get': 'list', 'post': 'create'}), name='advertiser-list'),
    path('advertisers/<int:pk>/', views.AdvertiserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='advertiser-detail'),
    path('locations/', views.LocationViewSet.as_view({'get': 'list', 'post': 'create'}), name='location-list'),
    path('locations/<int:pk>/', views.LocationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='location-detail'),
    path('campaigns/', views.AdCampaignViewSet.as_view({'get': 'list', 'post': 'create'}), name='campaign-list'),
    path('campaigns/<int:pk>/', views.AdCampaignViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='campaign-detail'),
    path('impressions/', views.AdImpressionViewSet.as_view({'get': 'list', 'post': 'create'}), name='impression-list'),
    path('impressions/<int:pk>/', views.AdImpressionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='impression-detail'),
    path('clicks/', views.AdClickViewSet.as_view({'get': 'list', 'post': 'create'}), name='click-list'),
    path('clicks/<int:pk>/', views.AdClickViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='click-detail'),
    path('transactions/', views.TransactionViewSet.as_view({'get': 'list', 'post': 'create'}), name='transaction-list'),
    path('transactions/<int:pk>/', views.TransactionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='transaction-detail'),
]
