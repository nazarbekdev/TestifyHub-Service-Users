from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from service.models import BotUser
from service.serializers import BotUserSerializer


class BotUserInfo(APIView):

    def get(self, request, telegram_id):
        try:
            user = BotUser.objects.get(telegram_id=telegram_id)
            serializer = BotUserSerializer(user)
            return Response(serializer.data)
        except BotUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
