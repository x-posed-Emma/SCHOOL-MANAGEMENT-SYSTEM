from django.contrib import admin
from .models import News,Annoncement,Student,Teacher,CustomUser

app_name = 'app1'

@admin.register(News)
class News(admin.ModelAdmin):
    list_display = ("News_Title", "News_Image", "News_Body", "Date")

@admin.register(Annoncement)
class Announcements(admin.ModelAdmin):
    list_display = ("Title",  "Body", "Date")

@admin.register(Student)
class Students(admin.ModelAdmin):
    list_display = ("user",  "grade")

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'grade', 'school_name')     

@admin.register(Teacher)
class Teachers(admin.ModelAdmin):
    list_display = ("user",  "subject_specialization")

@admin.register(CustomUser)
class CustomUsers(admin.ModelAdmin):
    list_display = ("username", "user_type")

