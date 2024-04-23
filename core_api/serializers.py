from rest_framework import serializers
from .models import Category, Product, Cart, CartItem, Tenant, Wishlist


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_items_read = CartItemSerializer(many=True, read_only=True)
    cart_items = CartItemSerializer(many=True, write_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        cart_data = validated_data.pop('cart_items', [])
        instance, _ = Cart.objects.get_or_create(**validated_data)
        for items in cart_data:
            CartItem.objects.create(cart=instance, **items)
        return instance

    def update(self, instance, validated_data):
        carts_item = validated_data.pop('carts_item', [])
        instance = super().update(instance, validated_data)
        for items in carts_item:
            CartItem.objects.update_or_create(
                cart=instance, id=items.get('id'), defaults=items)


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'
