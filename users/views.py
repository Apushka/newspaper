from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from users.serializers import RegisterSerializer


class RegisterUserAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

