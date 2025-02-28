from rest_framework import generics, status
from rest_framework.response import Response
from quiz.models import QuizQuestion, QuizUser, Database, Subject
from quiz.serializers import QuizQuestionSerializer, QuizUserSerializer, SubjectSerializer, DatabaseSerializer


class QuizQuestionListCreateAPIView(generics.GenericAPIView):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer

    def get(self, request, *args, **kwargs):
        # URL’dan fan_id va baza_id’ni olish
        fan_id = kwargs.get('fan_id')
        baza_id = kwargs.get('baza_id')

        if fan_id and baza_id:
            # Fan va baza bo‘yicha 10 ta tasodifiy savol
            questions = self.queryset.filter(baza_id=baza_id, fan_id=fan_id).order_by('?')[:10]
            if not questions.exists():
                return Response({"detail": "Bu fan va baza uchun savollar topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Agar fan_id yoki baza_id berilmagan bo‘lsa, barcha savollar
            questions = self.queryset.all()

        serializer = self.get_serializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # POST: Yangi savol yaratish
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuizQuestionRetrieveUpdateAPIView(generics.GenericAPIView):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        # GET: Bitta savolni olish
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        # PATCH: Savolni qisman yangilash
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class QuizUserListCreateAPIView(generics.GenericAPIView):
    queryset = QuizUser.objects.all()
    serializer_class = QuizUserSerializer

    def get(self, request, *args, **kwargs):
        # GET: Barcha natijalar yoki filterlangan natija
        telegram_id = request.query_params.get('telegram_id')
        baza = request.query_params.get('baza')
        fan = request.query_params.get('fan')
        if telegram_id and baza and fan:
            results = self.queryset.filter(telegram_id=telegram_id, baza=baza, fan=fan)
        else:
            results = self.queryset.all()
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # POST: Yangi natija qo‘shish yoki mavjudni yangilash
        telegram_id = request.data.get('telegram_id')
        baza = request.data.get('baza')
        fan = request.data.get('fan')
        natija = request.data.get('natija')
        ism = request.data.get('ism', 'Noma\'lum')

        quiz_user = self.queryset.filter(telegram_id=telegram_id, baza=baza, fan=fan).first()
        if quiz_user:
            # Mavjud bo‘lsa, yangilash
            quiz_user.natija = natija
            quiz_user.urinishlar += 1
            quiz_user.save()
            serializer = self.get_serializer(quiz_user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Yangi natija yaratish
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class QuizUserRetrieveUpdateAPIView(generics.GenericAPIView):
    queryset = QuizUser.objects.all()
    serializer_class = QuizUserSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        # GET: Bitta natijani olish
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        # PATCH: Natijani qisman yangilash
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class SubjectsAPIView(generics.GenericAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    def get(self, request):
        result = self.queryset.all()
        serializer = self.get_serializer(result, many=True)
        return Response(serializer.data)


class DatabaseAPIView(generics.GenericAPIView):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer
    
    def get(self, request):
        result = self.queryset.all()
        serializer = self.get_serializer(result, many=True)
        return Response(serializer.data)
    