from rest_framework import status, viewsets, mixins, filters
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsAdmin, CustomPermission
from .serializers import RegistrationSerializer, TokenSerializer, UserSerializer
from .pagination import CustomPagination

from reviews.models import User


class SignUpAPIView(APIView):
    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data
        # Если пользователь существует отправить ему код подтверждения не пытаясь создать нового
        if (
                User.objects.filter(username=user.get('username'), email=user.get('email')).exists()
        ):
            new_user = User.objects.get(username=user.get('username'))
            new_user.email_user('Confirmation code', new_user.generate_confirm_code())
            return Response('Check email', status=status.HTTP_200_OK)
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        new_user = User.objects.get(username=user.get('username'))
        new_user.email_user('Confirmation code', new_user.generate_confirm_code())
        return Response(serializer.data, status=status.HTTP_200_OK)


class TokenAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = TokenSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, username=data.get('username'))
        if user.check_confirm_code(data.get('confirmation_code')):
            return Response(user.token, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsAdmin,)
    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)


class GenericUpdateViewSet(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    pass


class MeDetailsViewSet(GenericUpdateViewSet):
    print('AAAAAA')
    serializer_class = UserSerializer
    permission_classes = (CustomPermission,)

    def get_object(self):
        return self.request.user
