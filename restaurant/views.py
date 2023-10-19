from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes

@renderer_classes([JSONRenderer])
class MenuItemsView(generics.ListCreateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer

@renderer_classes([JSONRenderer])
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer