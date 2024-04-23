from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Category, Product, Cart, CartItem, Tenant, Wishlist
from .serializers import CategorySerializer, ProductSerializer, CartSerializer, TenantSerializer, WishlistSerializer, CartItemSerializer


def get_message():
    return "Tenant id required in query params"


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        query_set = super().get_queryset()
        tenant_id = self.request.query_params.get('tenant_id')
        if tenant_id:
            query_set = query_set.filter(tenant_id=tenant_id)
        # else:
        #     raise PermissionError(f"{get_message()}")
        return query_set


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [AllowAny]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        query_set = super().get_queryset()
        tenant_id = self.request.query_params.get('tenant_id')
        if tenant_id:
            query_set = query_set.filter(tenant_id=tenant_id)
        # else:
        #     raise PermissionError(f"{get_message()}")
        return query_set


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        query_set = super().get_queryset()
        tenant_id = self.request.query_params.get('tenant_id')
        if tenant_id:
            query_set = query_set.filter(tenant_id=tenant_id)
        # else:
        #     raise PermissionError(f"{get_message()}")
        return query_set


class TenantViewset(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [AllowAny]
