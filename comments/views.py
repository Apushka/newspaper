from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from comments.permissions import HasCommentsPermissionOrReadOnly
from comments.pagination import CommentsPagination


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, HasCommentsPermissionOrReadOnly,)
    pagination_class = CommentsPagination

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user
        return super(CommentModelViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request.data['author'] = instance.author
        request.data['new'] = instance.new.pk
        return super(CommentModelViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(CommentModelViewSet, self).destroy(request, *args, **kwargs)
