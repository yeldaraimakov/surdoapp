from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include('surdoapp.surdoadmin.urls')),

    path('api/words/', include('surdoapp.surdoadmin.api.urls')),
]
