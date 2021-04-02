from django.urls import path

from toDoApp.views import index, add_new_todo, all_todos, delete, sort, search, edit

urlpatterns = [
    path('', index, name='index'),
    path('submit/<int:pk>', add_new_todo, name='submit'),
    path('list', all_todos, name='todos_list'),
    path('delete/<int:pk>', delete, name='delete'),
    path('sort', sort, name='sort'),
    path('search', search, name='search'),
    path('edit/<int:pk>', edit, name='edit')
]
