from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from service.models import OTM2025
from service.serializers import OTM2025Serializer


"""
    Bu Api barcha fanlarni qaytarish uchun.
"""


class YonalishView(GenericAPIView):
    serializer_class = OTM2025Serializer

    def get(self, request, pk):
        frst = int(pk.split('-')[0])
        scnd = int(pk.split('-')[1])
        data = OTM2025.objects.filter(fan1_id=frst, fan2_id=scnd)
        data_serializer = OTM2025Serializer(data, many=True)
        return Response({'data': data_serializer.data})
