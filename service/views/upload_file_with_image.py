import os
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from service.functions.read_from_pdf import test_pdf_read_text, test_pdf_read_image
from service.models import Question
from service.serializers import DocumentSerializer


"""
    Bu Api pdf fayldagi barcha testlarni bazaga saqlab olish uchun.
"""


class UploadFileWithImageView(GenericAPIView):
    serializer_class = DocumentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            saved_document = serializer.instance
            document_loc = saved_document.document.path

            try:
                data_text = test_pdf_read_text(document_loc)
                data_image = test_pdf_read_image(document_loc)
                for i, text in enumerate(data_text):
                    image = data_image[i]
                    question = text.split('//')[1]
                    answer = text.split('//')[0]
                    Question.objects.create(
                        language_id=serializer.validated_data['language'].id,
                        subject_id=serializer.validated_data['subject'].id,
                        question=question,
                        image=image,
                        answer=answer,
                        answers='?'
                    )

                # os.remove(document_loc)
            except Exception as e:
                return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'success': True}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
