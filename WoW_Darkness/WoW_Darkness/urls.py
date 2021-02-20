from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
    path('mythic', include('mythic.urls')),
    path('nathria', include('nathria.urls')),
    path('FAQ', include('FAQ.urls')),
    path('sendMail', include('sendmail.urls')),
    path('torghast', include('torghast.urls')),
    path('leveling', include('leveling.urls')),
]
