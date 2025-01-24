from rest_framework import serializers
from service.models import Document, Subject, GenerateTest, Language, ServiceUser, CheckSheet, GenerateTestData, \
    DatabaseType, TitulUpload, CheckSheetResult, OTM2025, UserFile, BotUser, BlokTest, Natijalar


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceUser
        fields = '__all__'


class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'
        # read_only_fields = ('checked_file',)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class GenerateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class GenerateTestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenerateTestData
        fields = '__all__'


class TestGeneratePDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenerateTest
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class UserFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFile
        fields = ['user', 'file']


class UserFileDownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFile
        fields = "__all__"


class CheckSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckSheet
        fields = ['user', 'file', 'book_id']


class CheckSheetResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckSheetResult
        fields = '__all__'


class DatabaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseType
        fields = '__all__'


class TitulUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitulUpload
        fields = '__all__'


class OTM2025Serializer(serializers.ModelSerializer):
    class Meta:
        model = OTM2025
        fields = '__all__'


class BlokTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlokTest
        fields = '__all__'


class NatijalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Natijalar
        fields = '__all__'
         