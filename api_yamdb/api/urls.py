from django.urls import path, include
from rest_framework import routers

from .views import AdminUserViewSet, SignUpAPIView, TokenAPIView, MeDetailsViewSet

router = routers.DefaultRouter()

#router.register('users/me/', MeDetailsViewSet, basename='MeDetail')
router.register('users', AdminUserViewSet, basename='AdminUser')

urlpatterns = [
    path('v1/users/me/', MeDetailsViewSet.as_view()),
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', SignUpAPIView.as_view()),
    path('v1/auth/token/', TokenAPIView.as_view()),
]
