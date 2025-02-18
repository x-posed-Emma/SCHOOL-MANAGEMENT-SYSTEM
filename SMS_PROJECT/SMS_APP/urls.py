from django.urls import path
from SMS_APP.views import NewsListView, AnnouncementListView,StudentDashboard
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from . import views

app_name = 'smsapp1'

urlpatterns = [
    path('', NewsListView.as_view(), name='home'),
    path('announcement/', AnnouncementListView.as_view(), name='announcement'),
    path('student_dash/', StudentDashboard.as_view(), name='student_dash'),
    path('register/', views.register, name='register'),
    path('completeprofile/', views.complete_profile, name='completeprofile'),
]+ static(settings.STATIC_URL)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)