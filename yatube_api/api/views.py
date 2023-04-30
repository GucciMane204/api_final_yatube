from django.shortcuts import get_object_or_404
from posts.models import Group, Post, User
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import AuthourOrReadOnly
from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthourOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthourOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=following__username', '=user__username')

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        queryset = user.follower.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
