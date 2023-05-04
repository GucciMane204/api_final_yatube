from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = (
            'id', 'text', 'author', 'image', 'pub_date', 'group', 'comments'
        )
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username',
                            queryset=User.objects.all(),
                            default=serializers.CurrentUserDefault()
                            )
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    def validate(self, data):
        if data['user'] == data['following']:
            raise serializers.ValidationError('Подписка невозможна.')
        return data

    class Meta:
        fields = 'user', 'following'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(), fields=('user', 'following'),
                message='Вы уже подписаны на данного автора.'
            )
        ]
