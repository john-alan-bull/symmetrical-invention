from rest_framework import serializers

from .models import Activity


class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return data


class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='pk', read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'name', 'duration_minutes', 'created_at']
