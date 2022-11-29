
from django.urls import path, include
from rest_framework import routers

from .views import (AdminUserViewSet, SignUpAPIView,
                    TokenAPIView, MeDetailsViewSet,
                    CommentViewSet, ReviewViewSet,
                    CategoryViewSet, GenreViewSet, TitlesViewSet)

router = routers.DefaultRouter()

#router.register('users/me/', MeDetailsViewSet, basename='MeDetail')
router.register('users', AdminUserViewSet, basename='AdminUser')

urlpatterns = [
    path('v1/users/me/', MeDetailsViewSet.as_view()),
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', SignUpAPIView.as_view()),
    path('v1/auth/token/', TokenAPIView.as_view()),

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'categories', CategoryViewSet, basename='Category')
router_v1.register(r'genres', GenreViewSet, basename='Genre')
router_v1.register(r'titles', TitlesViewSet, basename='Title')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('api/', include('api.urls')),
]
