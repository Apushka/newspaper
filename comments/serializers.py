from rest_framework import serializers
from comments.models import Comment
from users.models import User
from news.models import New


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    new = serializers.SlugRelatedField(slug_field='id', queryset=New.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'created', 'content', 'author', 'new')