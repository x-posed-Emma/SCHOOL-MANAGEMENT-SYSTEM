# Generated by Django 5.0.7 on 2025-01-23 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SMS_APP', '0002_alter_student_age_alter_teacher_age_annoncement_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='Author',
        ),
    ]
