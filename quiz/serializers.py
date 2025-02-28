from rest_framework import serializers
from quiz.models import Subject, Database, QuizQuestion, QuizUser

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']
        ref_name = 'QuizSubjectSerializer'


class DatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = ['id', 'name']
        ref_name = 'QuizDatabaseSerializer'

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ['id', 'baza', 'fan', 'savol', 'javoblar', 'javob', 'image']


class QuizUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizUser
        fields = ['id', 'ism', 'telegram_id', 'baza', 'fan', 'natija', 'urinishlar']