from django.urls import path

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
from app.views import FileList, file_content

urlpatterns = [
    path('', FileList.as_view(), name='file_list'),
    path('<str:date>', FileList.as_view(), name='file_list'),
    path('file/<str:name>', file_content, name='file_content'),
]
