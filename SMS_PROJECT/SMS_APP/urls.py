from django.urls import path
from SMS_APP.views import NewsListView, AnnouncementListView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin



urlpatterns = [
    path('', NewsListView.as_view(), name='home'),
    path('announcement/', AnnouncementListView.as_view(), name='announcement'),
]+ static(settings.STATIC_URL)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)