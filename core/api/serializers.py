from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from posts.models import Post

class UserSerializer(ModelSerializer):
    class Meta:
        model =User
        fields = ['username','email']



class PostSerializers(ModelSerializer):
    # author = UserSerializer()
    class Meta:
        model = Post
        fields = ['id','author','title','body','created','update']
        # depth = 1

