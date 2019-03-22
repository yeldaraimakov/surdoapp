from django.urls import path
from surdoapp.admin_side.api import views

urlpatterns = [
    path('<int:cat>/', views.SurdoWordsByCategory.as_view(), name='words_by_category'),
]
