from rest_framework import viewsets

from User.models import User
from User.serializers import (UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()