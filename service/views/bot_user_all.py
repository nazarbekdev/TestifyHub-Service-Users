from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from service.models import BotUser
from service.serializers import BotUserSerializer


class BotUsersAll(APIView):

    def get(self, request):
        try:
            # Barcha foydalanuvchilarni olish
            users = BotUser.objects.all()
            # Ma'lumotlarni serialize qilish
            serializer = BotUserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
