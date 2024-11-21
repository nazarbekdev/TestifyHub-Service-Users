from rest_framework.views import APIView
from django.http import HttpResponse


"""
    Bu Api titul faylini yuklab olishi uchun.
"""


class DownloadTitulView(APIView):
    def get(self, request):
        file_path = '/Users/uzmacbook/Portfolio/TestifyHub-Service/media/files/template.pdf'
        file_name = 'files/template.pdf'
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
