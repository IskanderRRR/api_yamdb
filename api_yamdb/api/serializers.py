from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from reviews.models import Category, Comment, Genre, Review, Title, User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email',
                  'username',
                  'first_name',
                  'last_name',
                  'bio',
                  'role']

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('me не может быть username')
        return value

    def create(self, validated_data):
        # Использовать метод create_user, который мы
        # написали ранее, для создания нового пользователя.
        return User.objects.create_user(**validated_data)

class UserSerializerRole(UserSerializer):


    class Meta:
        model = User
        fields = ['email',
                  'username',
                  'first_name',
                  'last_name',
                  'bio',
                  'role']
        read_only_fields = ('role',)



class RegistrationSerializer(serializers.ModelSerializer):
    """ Сериализация регистрации пользователя и создания нового. """

    class Meta:
        model = User
        fields = ['email',
                  'username']

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('me не может быть username')
        return value

    def create(self, validated_data):
        # Использовать метод create_user, который мы
        # написали ранее, для создания нового пользователя.
        return User.objects.create_user(**validated_data)


class TokenSerializer(serializers.Serializer):
    username = serializers.SlugField(

    )

    class Meta:
        model = User
        fields = ['username',
                  'confirmation_code',
                  'token']
        read_only_fields = ('token',)


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    def validate_score(self, value):
        if 0 > value > 10:
            raise serializers.ValidationError('Оценка по 10-бальной шкале!')
        return value

    def validate(self, data):
        request = self.context['request']
        author = request.user
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if (
                request.method == 'POST'
                and Review.objects.filter(title=title, author=author).exists()
        ):
            raise ValidationError('Может существовать только один отзыв!')
        return data


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Comment
