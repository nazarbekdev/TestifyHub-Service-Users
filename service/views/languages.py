from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from service.models import Language
from service.serializers import LanguageSerializer

"""
    Api barcha tillarni qaytarish uchun.
"""


class LanguagesView(GenericAPIView):
    serializer_class = LanguageSerializer

    def get(self, request):
        data = Language.objects.all()
        data_serializer = LanguageSerializer(data, many=True)
        return Response({'data': data_serializer.data})
