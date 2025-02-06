from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm, StudentForm, TeacherForm
from .models import Student, Teacher, CustomUser, News, Annoncement

# @method_decorator(login_required, name='dispatch')
class NewsListView(ListView):
    model = News
    template_name = 'sms_app/news.html'  # Define your template name here
    context_object_name = 'news_list'

    def get_queryset(self):
        return News.objects.filter(Date__isnull=False).order_by('-Date')
    
    
class AnnouncementListView(ListView):
    model = Annoncement
    template_name = 'sms_app/announcement.html'  # Define your template name here
    context_object_name = 'announcement_list'

    
    
# def get_queryset(self):
    #     return Annoncement.objects.filter(Date__isnull=False).order_by('-Date')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  
            user.save()
            request.session['user_id'] = user.id  
            return redirect('smsapp1:completeprofile')  
    else:
        form = UserRegistrationForm()
    return render(request, 'forms/register.html', {'form': form})

def complete_profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('smsapp1:register')

    user = CustomUser.objects.get(id=user_id)
    
    if request.method == 'POST':
        if user.user_type == 'student':
            form = StudentForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = user
                profile.save()
        else:
            form = TeacherForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = user
                profile.save()

        return redirect('/')  

    else:
        form = StudentForm() if user.user_type == 'student' else TeacherForm()

    return render(request, 'forms/complete_profile.html', {'form': form})

