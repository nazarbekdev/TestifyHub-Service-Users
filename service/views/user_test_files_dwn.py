from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from service.models import UserFile
from service.serializers import UserFileDownloadSerializer


class UserTestFilesView(GenericAPIView):
    serializer_class = UserFileDownloadSerializer

    def get_queryset(self):
        user_id = self.kwargs['id']
        return UserFile.objects.filter(user=user_id)

    def get(self, request, id):
        # Querysetni olish va serializer qilish
        user_files = self.get_queryset()
        serializer = UserFileDownloadSerializer(user_files, many=True)
        return Response(serializer.data)
