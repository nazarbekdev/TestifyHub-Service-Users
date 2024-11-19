from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from service.serializers import TitulUploadSerializer


class TitulUploadAPIView(GenericAPIView):
    serializer_class = TitulUploadSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=200)
