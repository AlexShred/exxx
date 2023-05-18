from rest_framework import generics

from . import models
from . import serializers


class UserRegisterCreateAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        if user:
            models.Author.objects.create(
                user=user
            )