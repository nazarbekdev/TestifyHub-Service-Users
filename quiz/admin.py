from django.contrib import admin
from quiz.models import Database, Subject, QuizQuestion, QuizUser


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class DatabaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    

class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'savol',  'fan', 'baza', 'created_at')


class QuizUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'fan', 'baza', 'natija', 'urinishlar', 'created_at')
    

admin.site.register(Database, DatabaseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(QuizQuestion, QuizQuestionAdmin)
admin.site.register(QuizUser, QuizUserAdmin)
