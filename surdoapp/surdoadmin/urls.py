from django.urls import path

from surdoapp.surdoadmin import views

urlpatterns = [
    path('', views.WordListView.as_view(), name='words_list'),
    path('words/create/', views.WordFormView.as_view(), name='word_create'),
    path('words/update/<int:id>', views.WordFormView.as_view(), name='word_update'),
    path('words/delete/<int:id>', views.delete_word, name='word_delete'),
]
