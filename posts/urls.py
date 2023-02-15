from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet, PostListAPIView,CategoryListAPIView,ContributorListAPIView

from django.conf.urls.static import static
from django.conf import settings

router = SimpleRouter()
router.register('user', UserViewSet, basename='user')
router.register('', PostViewSet, basename='post')

urlpatterns = router.urls

urlpatterns += [
    path('v1/list-filter/', PostListAPIView.as_view()),
    path('category', CategoryListAPIView.as_view()),
    path('contributor', ContributorListAPIView.as_view()),
    # path('video', VideoListAPIView.as_view())
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
                 # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
                 # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)