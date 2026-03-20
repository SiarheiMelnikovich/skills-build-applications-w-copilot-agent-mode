from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from pymongo import MongoClient
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

client = MongoClient(host='localhost', port=27017)
db = client['octofit_db']

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        return list(db.users.find())

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    def get_queryset(self):
        return list(db.teams.find())

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    def get_queryset(self):
        return list(db.activities.find())

class LeaderboardViewSet(viewsets.ModelViewSet):
    serializer_class = LeaderboardSerializer
    def get_queryset(self):
        return list(db.leaderboard.find())

class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    def get_queryset(self):
        return list(db.workouts.find())

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/',
    })
