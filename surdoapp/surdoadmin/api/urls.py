from django.urls import path
from surdoapp.surdoadmin.api import views

urlpatterns = [
    path('', views.SurdoWordsByCategory.as_view(), name='words_by_category'),
]
