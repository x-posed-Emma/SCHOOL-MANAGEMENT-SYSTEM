from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    admission_number = models.CharField(max_length=100, unique=True)
    class_assigned = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True, related_name='students')
    address = models.TextField()
    phone_number = models.CharField(max_length=15, unique=True)
    guardian_name = models.CharField(max_length=255)
    guardian_phone_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='student_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.admission_number}"


class Teacher(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    subject_taught = models.ManyToManyField('Subject', related_name='teachers')
    profile_picture = models.ImageField(upload_to='teacher_pictures/', blank=True, null=True)
    date_joined = models.DateField()

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Example: "Grade 10", "Class A"
    class_teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='class_teacher')
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=20, unique=True)  # Example: "MTH101"
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"


class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='exams')
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='exams')
    date = models.DateField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.subject.name} - {self.class_assigned.name} - {self.date}"


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='results')
    marks_obtained = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.exam.subject.name} - {self.marks_obtained}/{self.exam.total_marks}"


class NewsPost(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='news_posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    images = models.ImageField(upload_to='news_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class NewsPostLike(models.Model):
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"


class NewsPostComment(models.Model):
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.post.title}"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Announcement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='announcements')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notify_all = models.BooleanField(default=True)

    def __str__(self):
        return self.title