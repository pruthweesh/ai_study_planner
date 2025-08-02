from rest_framework import serializers
from .models import Progress, Notification

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'user', 'subject', 'completed', 'updated_at']
        extra_kwargs = {
            'updated_at': {'read_only': True},
            'user': {'read_only': True}
        }

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'created_at', 'is_read']
        extra_kwargs = {
            'created_at': {'read_only': True},
            'user': {'read_only': True}
        }