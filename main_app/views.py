from rest_framework import viewsets
from main_app.models     import OrderItem
from main_app.serializers import OrderItemSerializer



class OrderItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
