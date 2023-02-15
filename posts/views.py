from .serializers import PostSerializer, UserSerializer,CategorySerializer,ContributorSerializer
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics
from .models import Post,Category,Video,Contributor
from .permissions import IsAuthorOrReadOnly


# Create your views here.
#Post________________________________________________
class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(is_active=True).order_by('-id')
    serializer_class = PostSerializer

#Category______________________________________________
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True).order_by('-id')
    serializer_class = CategorySerializer

#Users__________________________________________________
class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

#Contributor_____________________________________________
class ContributorViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

class ContributorListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Category.objects.filter(is_active=True).order_by('-id')
    serializer_class = ContributorSerializer