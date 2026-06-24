"""
Vistas del carrito de compras para TIENDA - UrbanGear.
Permite agregar, actualizar, eliminar y vaciar ítems del carrito.
"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.cart.models import Cart, CartItem
from apps.products.models import Product, ProductVariant
from .serializers import CartSerializer, CartItemSerializer


def get_or_create_cart(request):
    """Obtiene o crea el carrito activo — por usuario autenticado o por sesión."""
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        cart, _ = Cart.objects.get_or_create(
            session_key=request.session.session_key,
            user=None
        )
    return cart


class CartDetailView(APIView):
    """GET /api/cart/ — obtener el carrito actual del comprador."""
    permission_classes = [AllowAny]

    def get(self, request):
        cart       = get_or_create_cart(request)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class CartAddView(APIView):
    """POST /api/cart/add/ — agregar un producto al carrito de UrbanGear."""
    permission_classes = [AllowAny]

    def post(self, request):
        cart       = get_or_create_cart(request)
        product_id = request.data.get('product_id')
        variant_id = request.data.get('variant_id')
        quantity   = int(request.data.get('quantity', 1))

        try:
            product = Product.objects.get(id=product_id, available=True)
        except Product.DoesNotExist:
            return Response({'error': 'Producto no encontrado en UrbanGear'}, status=404)

        variant = None
        if variant_id:
            try:
                variant = ProductVariant.objects.get(id=variant_id, product=product)
            except ProductVariant.DoesNotExist:
                return Response({'error': 'Variante no disponible'}, status=404)

        # Si el ítem ya existe en el carrito, acumula la cantidad
        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            variant=variant,
            defaults={'quantity': quantity}
        )
        if not created:
            item.quantity += quantity
            item.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartRemoveView(APIView):
    """DELETE /api/cart/remove/<item_id>/ — eliminar un ítem del carrito."""
    permission_classes = [AllowAny]

    def delete(self, request, item_id):
        cart = get_or_create_cart(request)
        try:
            item = CartItem.objects.get(id=item_id, cart=cart)
            item.delete()
            return Response(CartSerializer(cart).data)
        except CartItem.DoesNotExist:
            return Response({'error': 'Ítem no encontrado en tu carrito'}, status=404)


class CartUpdateView(APIView):
    """PATCH /api/cart/update/<item_id>/ — cambiar la cantidad de un ítem."""
    permission_classes = [AllowAny]

    def patch(self, request, item_id):
        cart     = get_or_create_cart(request)
        quantity = int(request.data.get('quantity', 1))

        try:
            item = CartItem.objects.get(id=item_id, cart=cart)
        except CartItem.DoesNotExist:
            return Response({'error': 'Ítem no encontrado en tu carrito'}, status=404)

        if quantity <= 0:
            item.delete()
            return Response({'message': 'Ítem eliminado del carrito'})

        item.quantity = quantity
        item.save()
        return Response(CartSerializer(cart).data)


class CartClearView(APIView):
    """DELETE /api/cart/clear/ — vaciar el carrito por completo."""
    permission_classes = [AllowAny]

    def delete(self, request):
        cart = get_or_create_cart(request)
        cart.items.all().delete()
        return Response(CartSerializer(cart).data)
