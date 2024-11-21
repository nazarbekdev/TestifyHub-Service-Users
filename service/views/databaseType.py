from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from service.models import DatabaseType
from service.serializers import DatabaseTypeSerializer


"""
    Bu Api databaselarni qaytarish uchun.
"""


class DatabaseTypeView(GenericAPIView):
    serializer_class = DatabaseTypeSerializer

    def get(self, request):
        data = DatabaseType.objects.all()
        data_serializer = DatabaseTypeSerializer(data, many=True)
        return Response({'data': data_serializer.data})
