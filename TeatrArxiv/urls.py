from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TeatrArxivSerializer ,TeatrArxivListAPIView,TeatrArxivModelViewSet,TeatrArxivCategorySerializer,TeatrAxrivCategoryAPIView,TeatrArxivCategoryModelViewSet

from django.conf.urls.static import static
from django.conf import settings

# router = SimpleRouter()
# router.register('', TeatrArxivModelViewSet, basename='post')
# router.register('category', TeatrArxivModelViewSet, basename='post')
#
# urlpatterns = router.urls

urlpatterns = [
    path('', TeatrArxivListAPIView.as_view()),
    path('category/', TeatrAxrivCategoryAPIView.as_view())
]