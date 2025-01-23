from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .models import News, Annoncement

# @method_decorator(login_required, name='dispatch')
class NewsListView(ListView):
    model = News
    template_name = 'sms_app/newsview.html'  # Define your template name here
    context_object_name = 'news_list'

    def get_queryset(self):
        # Filter news to ensure each has an author and a date
        return News.objects.filter(Date__isnull=False).order_by('-Date')
    
    
class AnnouncementListView(ListView):
    model = Annoncement
    template_name = 'sms_app/announcement.html'  # Define your template name here
    context_object_name = 'announcement_list'

    def get_queryset(self):
        return Annoncement.objects.filter(Date__isnull=False).order_by('-Date')