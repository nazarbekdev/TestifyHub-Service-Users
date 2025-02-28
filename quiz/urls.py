from django.urls import path
from quiz.views import QuizQuestionListCreateAPIView, QuizQuestionRetrieveUpdateAPIView, QuizUserListCreateAPIView, QuizUserRetrieveUpdateAPIView, SubjectsAPIView, DatabaseAPIView


urlpatterns = [
    # fan_id va baza_id bilan savollar olish uchun
    path('questions/<int:fan_id>/<int:baza_id>/', QuizQuestionListCreateAPIView.as_view(), name='question-list'),
    # Yangi savol qo‘shish uchun umumiy endpoint
    path('questions/', QuizQuestionListCreateAPIView.as_view(), name='question-create'),
    # Bitta savolni olish yoki yangilash uchun
    path('questions/<int:id>/', QuizQuestionRetrieveUpdateAPIView.as_view(), name='question-retrieve-update'),
    path('results/', QuizUserListCreateAPIView.as_view(), name='result-list-create'),
    path('results/<int:id>/', QuizUserRetrieveUpdateAPIView.as_view(), name='result-retrieve-update'),
    path('subjects/', SubjectsAPIView.as_view(), name='subjects-list'),
    path('database-types/', DatabaseAPIView.as_view(), name='database-list'),
]
