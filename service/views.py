from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


class IndexView(GenericAPIView):
    serializer_class = ''

    def get(self, request):
        return Response('TestifyHub Service for users!')
