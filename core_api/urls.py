from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, CartViewSet, WishlistViewSet, CartItemViewSet

# Define router
router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'wishlists', WishlistViewSet)
router.register(r'cart-items', CartItemViewSet)

# Define app_name for namespacing
app_name = 'core_api'

urlpatterns = [
    # Base API URL
    path('api/', include(router.urls)),
]
