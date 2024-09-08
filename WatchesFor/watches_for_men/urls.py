from django.urls import path

from .models import Watches
from .views import *
from rest_framework import routers
urlpatterns = [
    path('catalog/', WatchesList.as_view(), name='watches_list'),
    path('catalog/<int:pk>/', WatchesDetail.as_view(), name='watches_detail'),
]

router = routers.SimpleRouter()
router.register('api/category', CategoryViewSet, basename='category')
router.register('api/maker', MakerViewSet, basename='maker')
router.register('api/watches', WatchesViewSet, basename='watches')
router.register('api/order', OrderViewSet, basename='order')
router.register('api/supplier', SupplierViewSet, basename='supplier')
router.register('api/supply', SupplyViewSet, basename='supply')
router.register('api/pos_order', PosOrderViewSet, basename='pos_order')
router.register('api/pos_supply', PosSupplyViewSet, basename='pos_supply')

urlpatterns += router.urls