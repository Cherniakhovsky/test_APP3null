from django.conf.urls import url
#from django.contrib import admin

from .views import(
    UserCreateAPIView,
    )

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    #url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    #url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
]