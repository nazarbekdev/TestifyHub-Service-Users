from django.urls import path
from .views import (GenerateTestView, ServiceTestUserView, DownloadFileAPIView, DownloadSheetFileAPIView,
                    GenerateTestDefaultKey, UploadDocumentView, UploadFileWithImageView, LanguagesView, SubjectsView,
                    UserInfo, CheckSheetView, DatabaseTypeView, DownloadTitulView, TitulUploadAPIView,
                    UserTestFilesView, UserCheckedFilesView, BotUserView, BotUserInfo,
                    BotUserPatchView)

urlpatterns = [
    path('subjects', SubjectsView.as_view(), name='subject'),  # mobile
    path('upload-file', UploadDocumentView.as_view(), name='upload_file'),  # admin
    path('upload-file-with-image', UploadFileWithImageView.as_view(), name='upload_file_with_image'),  # admin
    path('generate-test-random', GenerateTestView.as_view(), name='generate_test'),  # mobile
    path('generate-test-default', GenerateTestDefaultKey.as_view(), name='generate_test1'),  # mobile
    path('languages', LanguagesView.as_view(), name='languages'),  # mobile
    path('download-generated-file/<int:user_id>', DownloadFileAPIView.as_view(), name='download_user_file'),  # mobile
    path('download-checked-sheet/<str:user_name>', DownloadSheetFileAPIView.as_view(), name='download_user_file'),  # mobile
    path('service-user', ServiceTestUserView.as_view(), name='camtest_user'),  # mobile
    path('user-info/<int:id>', UserInfo.as_view(), name='user_info'),  # mobile
    path('check-sheet', CheckSheetView.as_view(), name='check_sheet'),  # mobile
    path('database-type', DatabaseTypeView.as_view(), name='database_type'),  # mobile
    path('download-titul', DownloadTitulView.as_view(), name='download_titul'),  # mobile
    path('titul-upload', TitulUploadAPIView.as_view(), name='titul_upload'),  # admin
    path('all-test-files/<int:id>', UserTestFilesView.as_view(), name='user_test'),  # mobile
    path('all-checked-files/<str:user_name>', UserCheckedFilesView.as_view(), name='user_checked_files'),  # mobile
    path('bot-user', BotUserView.as_view(), name='bot_user'),  # bot
    path('bot-user-info/<int:telegram_id>', BotUserInfo.as_view(), name='bot_user_info'),  # bot
    path('bot-user-patch/<int:telegram_id>', BotUserPatchView.as_view(), name='bot_user_patch'),  # bot
]
