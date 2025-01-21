import uuid
from django.db import models


# Create your models here


class Student(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Age = models.IntegerField(max_length=5)
    Profile_Picture = models.ImageField(upload_to=)
    Student_Class = models.CharField(max_length=10)
    Student_Email = models.EmailField()
    Guardian_Name = models.CharField(max_length=50)
    Guardian_phone_Number = models.CharField(max_length=11)
    Guardian_Address = models.CharField(max_length=50)
    State_Of_Origin = models.CharField(max_length=50)
    Local_Government = models.CharField(max_length=50)
    Country_Of_Origin = models.CharField(max_length=50)
    Town_Of_Origin = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    Post_In_School = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    Health_Issues = models.TextField()
    Registration_Date = models.DateTimeField(auto_now_add=True)
    



class Teacher(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Category = models.CharField(max_length=20)
    Profile_Picture = models.ImageField(upload_to=)
    Subject = models.CharField(max_length=20)
    Post = models.CharField(max_length=20)
    Age = models.IntegerField(max_length=15)
    Next_Of_Kin = models.CharField(max_length=100)
    Phone_Number= models.CharField(max_length=11)
    State_Of_Origin = models.CharField(max_length=50)
    Local_Government = models.CharField(max_length=50)
    Country_Of_Origin = models.CharField(max_length=50)
    Town_Of_Origin = models.CharField(max_length=50)
    Registration_Date = models.DateTimeField(auto_now_add=True)


class Admin(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Category = models.CharField(max_length=20)
    Profile_Picture = models.ImageField(upload_to=)
    Phone_Number= models.CharField(max_length=11)
    State_Of_Origin = models.CharField(max_length=50)
    Local_Government = models.CharField(max_length=50)
    Country_Of_Origin = models.CharField(max_length=50)
    Town_Of_Origin = models.CharField(max_length=50)



