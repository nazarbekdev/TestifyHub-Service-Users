from rest_framework.response import Response
from rest_framework.views import APIView

from service.models import CallNumber
from service.serializers import CallNumberSerializer


class CallNumberView(APIView):
    def get(self, request):
        number = CallNumber.objects.all()
        serializer = CallNumberSerializer(number, many=True)
        return Response(serializer.data)
