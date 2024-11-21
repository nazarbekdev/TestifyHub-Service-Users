from rest_framework.response import Response
from rest_framework.views import APIView
from service.models import ServiceUser

"""
    Bu Api TestifyHub ga birinchi bor tashfif buyurgan foydalanuvchilarni ro'yxatga olish uchun.
"""


class ServiceTestUserView(APIView):

    def post(self, request):
        user_name = ServiceUser.objects.latest('id')
        user_id = user_name.id
        user_n = f'AA{user_id+1111}'
        user_i = int(user_id) + 1
        serializer = ServiceUser(name=user_n)
        serializer.save()
        return Response({'id': user_i, 'name': user_n}, status=200)
        