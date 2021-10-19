import json
from json import loads

from pymongo import MongoClient
from rest_framework import viewsets

from User.models import User
from User.serializers import (UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        # serializer.save()

        client = MongoClient('localhost', 27017)
        db = client.djangoProject
        collection = db.User_user
        users = db.User_user
        print(serializer.data)
        serializer1 = json.dumps(serializer.data)
        serializer2 = loads(serializer1)
        users.insert_one(serializer2)





        # client = MongoClient('localhost', 27017)
        # db = client.RadugaMarket
        # collection = db.users2
        # users = db.users2
        # print(serializer.data)
        # serializer1 = json.dumps(serializer.data)
        # serializer2 = loads(serializer1)
        # users.insert_one(serializer2)