
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MinValueValidator, MaxLengthValidator, RegexValidator


class CustomUser(AbstractUser):
    USER_TYPES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    is_verified = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  
        blank=True
    )

class Student(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)

    Age = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=0)  
    Profile_Picture = models.ImageField(upload_to="student_profile/")
    grade = models.CharField(max_length=50, default=1)

    Guardian_Name = models.CharField(max_length=100)  
    Guardian_phone_Number = models.CharField(
        max_length=15,  
        validators=[RegexValidator(r'^\+?\d{10,15}$', message="Enter a valid phone number.")]
    )
    Guardian_Address = models.CharField(max_length=255)  

    State_Of_Origin = models.CharField(max_length=50)
    Local_Government = models.CharField(max_length=50)
    Country_Of_Origin = models.CharField(max_length=50)
    Town_Of_Origin = models.CharField(max_length=50)

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')

    Health_Issues = models.TextField(blank=True, null=True)  

    def __str__(self):
        return f"{self.user.username} - Grade {self.grade}"

class Teacher(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    IDENTIFICATION_CHOICES = [
        ('NID', 'National ID'),
        ('PASS', 'Passport'),
        ('DL', 'Driver’s License'),
        ('VOTER', 'Voter’s Card'),
        ('OTH', 'Other'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)

    Profile_Picture = models.ImageField(upload_to='teacher_profile/')
    subject_specialization = models.CharField(max_length=100, null=True)
    
    years_of_experience = models.PositiveIntegerField(validators=[MinValueValidator(0)], default=0)

    Age = models.PositiveIntegerField(validators=[MinValueValidator(18)], default=0)  

    Next_Of_Kin = models.CharField(max_length=100)

    Phone_Number = models.CharField(
        max_length=15, 
        validators=[RegexValidator(r'^\+?\d{10,15}$', message="Enter a valid phone number.")]
    )

    State_Of_Origin = models.CharField(max_length=50)
    Local_Government = models.CharField(max_length=50)
    Country_Of_Origin = models.CharField(max_length=50)
    Town_Of_Origin = models.CharField(max_length=50)

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')

    Health_Issues = models.TextField(blank=True, null=True)  

    identification_type = models.CharField(
        max_length=10, choices=IDENTIFICATION_CHOICES, verbose_name="Identification Type", default="NID"
    )
    identification_number = models.CharField(
        max_length=50, unique=True, verbose_name="ID Number", null=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.subject_specialization}"


class News(models.Model):
    News_Title = models.CharField(max_length=100)
    News_Image = models.ImageField(upload_to="news_image/")
    News_Body = models.TextField()
    Comment = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey('Student', on_delete=models.CASCADE, null=True , blank=True)

class Annoncement(models.Model):
    Title = models.CharField(max_length=100)
    Image = models.ImageField(upload_to="announcement_image/")
    Body = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    Teacher_Author = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True) 