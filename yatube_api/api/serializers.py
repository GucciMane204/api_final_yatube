from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
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
