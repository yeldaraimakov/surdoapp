from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='words_list', permanent=False)),

    path('django-admin/', admin.site.urls),

    path('admin/', include('surdoapp.admin_side.urls')),

    path('api/words/', include('surdoapp.admin_side.api.urls')),
]
