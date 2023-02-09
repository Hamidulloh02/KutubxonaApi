from django.shortcuts import render
from .serializers import TeatrArxivSerializer,TeatrArxivCategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics
from .permissions import IsAuthorOrReadOnly
from .models import TeatrArxiv,Category
# Create your views here.


class TeatrArxivModelViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = TeatrArxiv.objects.all()
    serializer_class = TeatrArxivSerializer

class TeatrArxivListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = TeatrArxiv.objects.filter(is_active=True).order_by('-id')
    serializer_class = TeatrArxivSerializer

class TeatrArxivCategoryModelViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = TeatrArxivCategorySerializer

class TeatrAxrivCategoryAPIView(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Category.objects.filter(is_active=True).order_by('-id')
    serializer_class = TeatrArxivCategorySerializer

