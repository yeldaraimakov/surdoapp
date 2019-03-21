from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include('surdoapp.admin_side.urls')),

    path('api/words/', include('surdoapp.admin_side.api.urls')),
]
