from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from service.models import BlokTest
from service.serializers import BlokTestSerializer


class BlockTestPatchView(GenericAPIView):
    serializer_class = BlokTestSerializer

    def patch(self, request, telegram_id):
        bot_user = get_object_or_404(BlokTest, telegram_id=telegram_id)
        serializer = self.get_serializer(bot_user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
