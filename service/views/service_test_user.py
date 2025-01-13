from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from service.models import ServiceUser
from service.serializers import UserSerializer

url = 'https://www.figma.com/design/YoMfTtCPqjygX9Jnx0ylBK/testify-hub?node-id=0-1&p=f&t=izjTGeQNzDX9hdOu-0'


class ServiceTestUserView(GenericAPIView, CreateModelMixin):
    queryset = ServiceUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_name = request.data.get('user_name')
        if ServiceUser.objects.filter(user_name=user_name).exists():
            return Response(
                {"error": "User with this username already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return self.create(request, *args, **kwargs)
