from django.urls import include, path
from rest_framework import routers

from .views import (CommentViewSet, ReviewViewSet,
                    CategoryViewSet, GenreViewSet, TitlesViewSet)


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
