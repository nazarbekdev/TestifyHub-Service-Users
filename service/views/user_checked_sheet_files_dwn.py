from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from service.models import CheckSheetResult
from service.serializers import CheckSheetResultSerializer


class UserCheckedFilesView(GenericAPIView):
    serializer_class = CheckSheetResultSerializer

    def get_queryset(self):
        user_name = self.kwargs['user_name']
        return CheckSheetResult.objects.filter(user=user_name)

    def get(self, request, user_name):
        # Querysetni olish va serializer qilish
        user_files = self.get_queryset()
        serializer = CheckSheetResultSerializer(user_files, many=True)
        return Response(serializer.data)
