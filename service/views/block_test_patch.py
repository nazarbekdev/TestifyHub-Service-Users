from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from service.models import BlokTest
from service.serializers import BlokTestSerializer


class BlockTestPatchView(GenericAPIView):
    serializer_class = BlokTestSerializer

    def patch(self, request, telegram_id):
        bot_user = BlokTest.objects.filter(telegram_id=telegram_id).order_by('-id').first()        
        
        if not bot_user:
            return Response({"error": "BlokTest topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(bot_user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
