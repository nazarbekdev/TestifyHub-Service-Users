from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from service.serializers import BlokTestSerializer


class BlockTestView(GenericAPIView):
    serializer_class = BlokTestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True}, status=200)
