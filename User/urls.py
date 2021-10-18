from django.urls import path

from User.views import UserViewSet

urlpatterns = [
    path('user/', UserViewSet.as_view(), name='users'),
]