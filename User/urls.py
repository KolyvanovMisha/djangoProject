from django.urls import include, path
from rest_framework.routers import DefaultRouter

from User.views import UserAPIView

# router_v1 = DefaultRouter()
# router_v1.register('users', UserAPIView, basename='users')
# router_v1.register('post', PostAPIView, basename='post')
#
# urlpatterns = [
#     path('v1/', include(router_v1.urls)),
# ]

urlpatterns = [
    path('user/', UserAPIView.as_view()),
]
