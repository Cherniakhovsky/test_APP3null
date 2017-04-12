from django.contrib.auth.models import User
from django.conf.urls import url
#from django.contrib import admin

from .serializers import (
    UserSerializer,
    UserCreateSerializer,
    UserLoginSerializer,
    )

from .views import(
    UserList, #UserAPIView,
    UserCreateAPIView,
    UserLoginAPIView
    )

urlpatterns = [
    url(r'^users/$', UserList.as_view(), name='users'),
    # url(r'^/users/$', UserList.as_view(queryset=User.objects.all(),
    #                                            serializer_class=UserSerializer),name='user-list'),
    url(r'^signin/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^signup/$', UserCreateAPIView.as_view(), name='register'),
    #url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    #url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
]