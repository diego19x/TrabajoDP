"""Serializers de reseñas de productos para TIENDA - UrbanGear."""
from rest_framework import serializers
from apps.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer de reseña con validación de rating y unicidad por usuario."""
    user     = serializers.StringRelatedField(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model            = Review
        fields           = ['id', 'user', 'username', 'rating', 'comment', 'created']
        read_only_fields = ['user', 'created']

    def validate_rating(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError('La calificación debe estar entre 1 y 5 estrellas')
        return value

    def validate(self, data):
        request = self.context['request']
        product = self.context['product']
        if Review.objects.filter(user=request.user, product=product).exists():
            raise serializers.ValidationError('Ya publicaste una reseña para este producto')
        return data
