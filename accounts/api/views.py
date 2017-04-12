from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import generics


from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
from rest_framework.views import APIView

#from django.contrib.auth.models import User
#from posts.api.permissions import IsOwnerOrReadOnly
#from posts.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination

User = get_user_model()

from .serializers import (
    UserSerializer,
    UserCreateSerializer,
    UserLoginSerializer,
    )


# class UserAPIView(APIView):
#     authentication_classes = authentication.TokenAuthentication  ###Am assuming you're authenticating via a token
#     def get(self, request):
#         """
#         Get user based on username.
#         Am getting only the username since that's the only field used above.
#         :param request:
#         :param format:
#         :return:
#         """
#         details = User.objects.all()
#         serializer = UserSerializer(details)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         """
#         Create a new user instance
#         :param request:
#         :param format:
#         :return:
#         """
#         serializer = UserSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

    # def get(self, request, *args, **kwargs):
    #     return self.__list_view(request) if 'pk' not in self.kwargs else self.__detail_view(request)

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminOrReadOnly,)

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser,)

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# class UserAPIView(APIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

    # # queryset = User.objects.all()
    # serializer_class = UserSerializer
    # #permission_classes = (IsAdminUser,)
    # def get(self, request):
    #         details = User.objects.all()
    #         serializer = UserSerializer(details)
    #         return Response(serializer.data)

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# class UserInvitationAPIView()