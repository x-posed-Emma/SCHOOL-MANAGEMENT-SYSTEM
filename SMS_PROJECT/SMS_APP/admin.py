from django.contrib import admin
from .models import News

app_name = 'app1'

@admin.register(News)
class Productss(admin.ModelAdmin):
    list_display = ("News_Title", "News_Image", "News_Body", "Date")
