from rest_framework import serializers
from news.models import New
from users.models import User
from comments.models import Comment

from comments.serializers import CommentSerializer


class NewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    comments = serializers.SerializerMethodField()

    class Meta:
        model = New
        fields = ('id', 'title', 'content', 'author', 'created', 'comments', 'likes_count', 'comments_count')

    def get_comments(self, obj):
        comments = Comment.objects.filter(new=obj)
        return CommentSerializer(comments[0:10], many=True).data

