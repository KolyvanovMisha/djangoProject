from rest_framework import viewsets
from User.serializers import (UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
