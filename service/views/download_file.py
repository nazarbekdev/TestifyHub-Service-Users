from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from service.models import UserFile


"""
    Bu Api foydalanuvchining generatsiya bo'lgan faylini yuklab olishi uchun.
"""


class DownloadFileAPIView(APIView):
    def get(self, request, user_id):
        user_file = UserFile.objects.filter(user=user_id).order_by('-id').first()

        if user_file is None:
            return Response({'success': False, 'message': "Foydalanuvchi uchun fayl topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        file_path = user_file.file.path
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{user_file.file.name}"'
            return response
