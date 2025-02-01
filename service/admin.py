from django.contrib import admin
from service.models import (Document, Question, Subject, Language, GenerateTest, ServiceUser, AnswerTest, UserFile,
                            Key, CheckSheet, CheckSheetResult, DatabaseType, GenerateTestData, TestControl,
                            SubjectCategory, BotUser, OTM2025, Fanlar, BlokTest,Natijalar)


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
    list_display = ('question', 'subject_id', 'subject_category_id', 'language_id', 'database_type_id', 'id')
    list_filter = ('subject_id', 'subject_category_id', 'database_type_id')
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
    list_display = ('id', 'name', 'user_name', 'telegram_id', 'balans', 'order', 'referral_link', 'invited_by', 'created_at')
    # readonly_fields = ('checked_file', 'telegram_id', 'user_name')
    list_filter = ('name', 'user_name', 'telegram_id', 'invited_by')
    date_hierarchy = 'created_at'


class OTM2025Admin(admin.ModelAdmin):
    list_display = ('id', 'yonalish_kodi', 'yonalish_nomi', 'fan1', 'fan2', 'created_at')
    list_filter = ('fan1', 'fan2')
    search_fields = ('yonalish_kodi', 'yonalish_nomi')


class FanlarAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomi')
    search_fields = ('nomi',)


class BlokTestAdmin(admin.ModelAdmin):
    list_display = ("id", "ism_familiya", "masked_phone", "viloyat", "fan1", "fan2", "rejalashtirilgan_vaqt", "status", "created_at")

    def masked_phone(self, obj):
        return obj.telefon_raqam[:-5] + "** **"

    masked_phone.short_description = "Telefon raqam"

    # Tahrirlash sahifasida telefon raqam to‘liq ko‘rinishi uchun
    fields = ("telegram_id", "ism_familiya", "telefon_raqam", "viloyat", "fan1", "fan2", "rejalashtirilgan_vaqt", "status")


class NatijalarAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'viloyat', 'blok1', 'blok2', 'majburiy', 'fan1', 'fan2', 'ball',  'created_at')
    list_filter = ('blok1', 'blok2', 'viloyat')
    date_hierarchy = 'created_at'


admin.site.register(Key, KeyAdmin)
admin.site.register(ServiceUser, ServiceUserAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectCategory, SubjectCategoryAdmin)
admin.site.register(UserFile, UserFileAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(AnswerTest, AnswerTestAdmin)
admin.site.register(CheckSheet, CheckSheetAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register((GenerateTest,))
admin.site.register(GenerateTestData, GenerateTestDataAdmin)
admin.site.register(DatabaseType, DatabaseTypeAdmin)
admin.site.register(TestControl, TestControlAdmin)
admin.site.register(CheckSheetResult, CheckSheetResultAdmin)
admin.site.register(BotUser, BotUserAdmin)
admin.site.register(OTM2025, OTM2025Admin)
admin.site.register(Fanlar, FanlarAdmin)
admin.site.register(BlokTest, BlokTestAdmin)
admin.site.register(Natijalar, NatijalarAdmin)
