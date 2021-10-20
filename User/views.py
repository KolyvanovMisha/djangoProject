from rest_framework.response import Response
from rest_framework.views import APIView
from mongo_connect import mongo_connection


class UserAPIView(APIView):

    def get(self, request):
        # Подключение к MongoDB
        collection = mongo_connection('USER')

        # Поиск по имени
        author = request.data['author']
        user = collection.find_one({"author": author})

        return Response((user['author']))

    def post(self, request):
        pass

    def put(self, request):
        pass

    def patch(self, request):
        pass

    def delete(self, request):
        pass
