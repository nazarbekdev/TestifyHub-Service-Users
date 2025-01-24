from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from service.models import BlokTest
from service.serializers import BlokTestSerializer


class BlockTestAll(APIView):

    def get(self, request):
        try:
            users = BlokTest.objects.all()
            if not users.exists():
                return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = BlokTestSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
