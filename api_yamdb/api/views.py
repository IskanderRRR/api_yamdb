from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from reviews.models import Category, Genre, Title
from .filters import TitlesFilter
from .serializers import (CategorySerializer,
                          GenreSerializer,
                          TitleCreateSerializer,
                          TitleListSerializer,)


class TitlesViewSet(viewsets.ModelViewSet):
    """
    Предоставляет CRUD-действия для произведений.
    """
    queryset = Title.objects.all()
    serializer_class = TitleListSerializer
    # permission_classes = дописать пермишен
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitlesFilter
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return TitleCreateSerializer
        return TitleListSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Возвращает список, создает новые и удаляет существующие категории.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    # permission_classes = дописать пермишен
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)

    @action(detail=False,
            methods=['delete'],
            url_path=r'(?P<slug>[-\w]+)', )
            # permission_classes= )
    def slug(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreViewSet(viewsets.ModelViewSet):
    """
    Возвращает список, создает новые и удаляет существующие жанры.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    # permission_classes = дописать пермишен
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)

    @action(detail=False,
            methods=['delete'],
            url_path=r'(?P<slug>[-\w]+)', )
            # permission_classes= )
    def slug(self, request, slug):
        genre = get_object_or_404(Genre, slug=slug)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
