"""
Serializers del catálogo de productos para TIENDA - UrbanGear.
Convierte los modelos Category, Product y ProductVariant a formato JSON.
"""
from rest_framework import serializers
from apps.products.models import Category, Product, ProductVariant


class CategorySerializer(serializers.ModelSerializer):
    """Serializer para categorías deportivas de UrbanGear."""
    class Meta:
        model  = Category
        fields = ['id', 'name', 'slug', 'image']


class ProductVariantSerializer(serializers.ModelSerializer):
    """Serializer para variantes de producto (talle/color) con precio final."""
    final_price = serializers.SerializerMethodField()

    class Meta:
        model  = ProductVariant
        fields = ['id', 'size', 'color', 'stock', 'extra_price', 'final_price']

    def get_final_price(self, obj):
        return obj.get_final_price()


class ProductSerializer(serializers.ModelSerializer):
    """Serializer detallado de producto — incluye variantes y rating promedio."""
    category       = CategorySerializer(read_only=True)
    category_id    = serializers.PrimaryKeyRelatedField(
                         queryset=Category.objects.all(),
                         source='category',
                         write_only=True
                     )
    variants       = ProductVariantSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model  = Product
        fields = [
            'id', 'name', 'slug', 'description',
            'price', 'stock', 'image', 'available',
            'category', 'category_id',
            'variants', 'average_rating',
            'created', 'updated',
        ]

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class ProductListSerializer(serializers.ModelSerializer):
    """Serializer liviano para listados — sin variantes completas ni reseñas."""
    category_name  = serializers.CharField(source='category.name', read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model  = Product
        fields = [
            'id', 'name', 'slug', 'price', 'image',
            'available', 'stock', 'category_name', 'average_rating',
        ]

    def get_average_rating(self, obj):
        return obj.get_average_rating()
