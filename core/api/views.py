from django.shortcuts import render
from api.serializers import PostSerializers
from posts.models import Post
from rest_framework.views import APIView,Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permission import IsAuthorOrReadOnly
# Create your views here.



class PostApiListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializers




class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializers

