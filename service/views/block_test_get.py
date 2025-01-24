from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from service.models import BlokTest
from service.serializers import BlokTestSerializer


class BlockTestInfo(APIView):

    def get(self, request, telegram_id):
        try:
            # Eng oxirgi yozuvni olish
            user = BlokTest.objects.filter(telegram_id=telegram_id).order_by('-created_at').first()
            if not user:
                return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

            # Ma'lumotni serialize qilish
            serializer = BlokTestSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
