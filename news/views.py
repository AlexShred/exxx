from django.http import JsonResponse
from rest_framework import generics
from rest_framework import permissions
from rest_framework import pagination
from rest_framework import filters
from rest_framework.generics import get_object_or_404

from . import models
from . import serializers
from . import permissions as perm


class NewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = pagination.PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['created']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NewsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = [perm.IsAuthorOrIsReadOnly]


class NewsCommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author, news_id=self.kwargs['news_id'])


class NewsCommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [perm.IsAuthorOrIsReadOnly]


class StatusListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [perm.IsAuthorOrIsReadOnly]


class StatusRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [perm.IsAuthorOrIsReadOnly]


class NewsStatusCreateAPIView(generics.CreateAPIView):
    queryset = models.NewsStatus.objects.all()
    serializer_class = serializers.NewsStatusSerializer
    # permission_classes = [perm.IsAuthorOrIsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            reply=get_object_or_404(models.News, pk=self.kwargs['news_id']),
            profile=self.request.user.profile
        )


class CommentStatusCreateAPIView(generics.CreateAPIView):
    queryset = models.CommentStatus.objects.all()
    serializer_class = serializers.CommentStatusSerializer
    # permission_classes = [perm.IsAuthorOrIsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            reply=get_object_or_404(models.News, pk=self.kwargs['news_id']),
            profile=self.request.user.profile
        )