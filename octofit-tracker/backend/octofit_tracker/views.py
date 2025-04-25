from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://bookish-carnival-r4g7wq4q6999357r4-8000.app.github.dev/'
    return Response({
        'users': base_url + 'api/users/',
        'teams': base_url + 'api/teams/',
        'activities': base_url + 'api/activities/',
        'leaderboard': base_url + 'api/leaderboard/',
        'workouts': base_url + 'api/workouts/'
    })