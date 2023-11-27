from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from news.permissions import HasNewPermissionsOrReadOnly
from news.pagination import NewsPagination

from news.models import New
from news.serializers import NewSerializer


class IndexView(TemplateView):
    template_name = 'newspaper/index.html'


class NewModelViewSet(ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = (IsAuthenticated, HasNewPermissionsOrReadOnly)
    pagination_class = NewsPagination

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user
        return super(NewModelViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        request.data['author'] = instance.author
        return super(NewModelViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(NewModelViewSet, self).destroy(request, *args, **kwargs)


class LikeOrUnlikeAPIView(UpdateAPIView):
    queryset = New.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = NewSerializer

    def update(self, request, *args, **kwargs):
        new_id = kwargs.get('pk')
        news = New.objects.filter(pk=new_id)

        if not news.exists():
            return Response({'new_id': 'Новость не найдена'}, status.HTTP_400_BAD_REQUEST)

        new, is_added = New.like_or_dislike(new_id, self.request.user)
        serializer = self.get_serializer(new)

        status_code = status.HTTP_201_CREATED if is_added else status.HTTP_200_OK

        return Response(serializer.data, status=status_code)



