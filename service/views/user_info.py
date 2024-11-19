from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from service.models import ServiceUser
from service.serializers import CamTestUserSerializer  # Import your serializer


class UserInfo(APIView):

    def get(self, request, id):
        try:
            user = ServiceUser.objects.get(id=id)
            serializer = CamTestUserSerializer(user)  # Serialize the user object
            return Response(serializer.data)
        except ServiceUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
