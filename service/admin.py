from django.contrib import admin
from service.models import (Document, Question, Subject, Language, GenerateTest, ServiceUser, AnswerTest, UserFile, CallNumber,
                        Key, CheckSheet, CheckSheetResult, DatabaseType, GenerateTestData, TestControl, SubjectCategory,
                        BotUser)


class CallNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class DatabaseTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class SubjectCategoryAdmin(admin.ModelAdmin):
    list_filter = ('subject__name', 'name')
    list_display = ('id', 'name', 'subject')


class TestControlAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'category', 'question_limit', 'created_at')
    list_filter = ('category', 'subject')


class AnswerTestAdmin(admin.ModelAdmin):
    search_fields = ('book_code',)
    list_display = ('id', 'book_code', 'answers', 'created_at')
    date_hierarchy = 'created_at'


class UserFileAdmin(admin.ModelAdmin):
    search_fields = ('user',)
    list_display = ('id', 'user', 'file', 'created_at')


class ServiceUserAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'limit', 'status', 'created_at')
    list_filter = ('status',)


class DocumentAdmin(admin.ModelAdmin):
    search_fields = ('subject',)
    list_display = ('id', 'file', 'language', 'subject', 'subject_category', 'created_at')
    list_filter = ('subject', 'language', 'subject_category')


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ('question',)
    list_display = ('id', 'question', 'subject_id', 'subject_category_id', 'language_id', 'database_type_id')
    list_filter = ('subject_id', 'subject_category_id')
    date_hierarchy = 'created_at'


class CheckSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book_id', 'file', 'created_at')
    search_fields = ('book_id', 'file')
    list_filter = ('user',)


class CheckSheetResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file', 'created_at')
    search_fields = ('file',)
    list_filter = ('user',)
    date_hierarchy = 'created_at'


class KeyAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam_type', 'keys', 'created_at')


class GenerateTestDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_books', 'subject1', 'subject2', 'language', 'created_at')
    list_filter = ('subject1', 'subject2', 'language')
    search_fields = ('number_books',)


class BotUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_name', 'telegram_id', 'limit', 'checked_file', 'created_at')
    # readonly_fields = ('checked_file', 'telegram_id', 'user_name')


admin.site.register(Key, KeyAdmin)
admin.site.register(ServiceUser, ServiceUserAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectCategory, SubjectCategoryAdmin)
admin.site.register(UserFile, UserFileAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(AnswerTest, AnswerTestAdmin)
admin.site.register(CheckSheet, CheckSheetAdmin)
admin.site.register(CallNumber, CallNumberAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register((GenerateTest,))
admin.site.register(GenerateTestData, GenerateTestDataAdmin)
admin.site.register(DatabaseType, DatabaseTypeAdmin)
admin.site.register(TestControl, TestControlAdmin)
admin.site.register(CheckSheetResult, CheckSheetResultAdmin)
admin.site.register(BotUser, BotUserAdmin)
