# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import CustomUser

# @receiver(post_save, sender=CustomUser)
# def activate_verified_users(sender, instance, **kwargs):
#     # Automatically activate the user when they are verified
#     if instance.is_verified and not instance.is_active:
#         instance.is_active = True
#         instance.save()

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Student, Teacher

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # Only create the profile if the user is newly created
        if instance.user_type == 'student':
            Student.objects.create(user=instance)
        elif instance.user_type == 'teacher':
            Teacher.objects.create(user=instance)        