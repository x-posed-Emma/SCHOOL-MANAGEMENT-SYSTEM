from django.urls import path
from SMS_APP.views import NewsListView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("URL routing works!")


urlpatterns = [
    path('', NewsListView.as_view(), name='home'),
]+ static(settings.STATIC_URL)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)