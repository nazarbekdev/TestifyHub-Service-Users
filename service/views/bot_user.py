from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from service.serializers import BotUserSerializer
"""
    Bu Api camtestuz_bot ga tashfif buyurgan foydalanuvchilarni ro'yxatga olish uchun.
"""


class BotUserView(GenericAPIView):
    serializer_class = BotUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
