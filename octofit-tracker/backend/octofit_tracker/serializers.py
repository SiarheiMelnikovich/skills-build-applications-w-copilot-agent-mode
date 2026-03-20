from rest_framework import serializers
from bson import ObjectId

# Helper to convert ObjectId to string
class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.Serializer):
    id = ObjectIdField(source='_id', read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    team = serializers.CharField()

class TeamSerializer(serializers.Serializer):
    id = ObjectIdField(source='_id', read_only=True)
    name = serializers.CharField()
    members = serializers.ListField(child=serializers.CharField())

class ActivitySerializer(serializers.Serializer):
    id = ObjectIdField(source='_id', read_only=True)
    user = serializers.CharField()
    activity = serializers.CharField()
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    id = ObjectIdField(source='_id', read_only=True)
    user = serializers.CharField()
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    id = ObjectIdField(source='_id', read_only=True)
    name = serializers.CharField()
    level = serializers.CharField()
