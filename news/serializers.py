from rest_framework import serializers
from django.db.utils import IntegrityError

from . import models


class NewsSerializer(serializers.ModelSerializer):
    get_status = serializers.ReadOnlyField()

    class Meta:
        model = models.News
        fields = "__all__"
        read_only_fields = ['author', ]


class CommentSerializer(serializers.ModelSerializer):
    get_status = serializers.ReadOnlyField()

    class Meta:
        model = models.Comment
        fields = "__all__"
        read_only_fields = ['author', 'news']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = '__all__'


class NewsStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsStatus
        fields = "__all__"
        read_only_fields = ['profile', 'news']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            new_reaction_type = validated_data.pop('reaction')
            instance = self.Meta.model.objects.get(**validated_data)
            instance.reaction = new_reaction_type
            instance.save()
            return instance


class CommentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentStatus
        fields = "__all__"
        read_only_fields = ['profile', 'news']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            new_reaction_type = validated_data.pop('reaction')
            instance = self.Meta.model.objects.get(**validated_data)
            instance.reaction = new_reaction_type
            instance.save()
            return instance
