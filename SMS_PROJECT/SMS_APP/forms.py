from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Student, Teacher

class UserRegistrationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPES, widget=forms.RadioSelect)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'user', 'Profile_Picture', 'Age', 'grade', 'Guardian_Name', 
            'Guardian_phone_Number', 'Guardian_Address', 'State_Of_Origin', 
            'Local_Government', 'Country_Of_Origin', 'Town_Of_Origin', 
            'Gender', 'Health_Issues', 
        ]
        widgets = {
            'user': forms.Select(attrs={'class': 'custom-input'}),
            'Profile_Picture': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'Age': forms.NumberInput(attrs={'class': 'custom-input', 'min': 3}),
            'grade': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Enter grade'}),
            'Guardian_Name': forms.TextInput(attrs={'class': 'custom-input'}),
            'Guardian_phone_Number': forms.TextInput(
                attrs={'class': 'custom-input', 'placeholder': 'Enter guardian phone number'}
            ),
            'Guardian_Address': forms.TextInput(attrs={'class': 'custom-input'}),
            'State_Of_Origin': forms.TextInput(attrs={'class': 'custom-input'}),
            'Local_Government': forms.TextInput(attrs={'class': 'custom-input'}),
            'Country_Of_Origin': forms.TextInput(attrs={'class': 'custom-input'}),
            'Town_Of_Origin': forms.TextInput(attrs={'class': 'custom-input'}),
            'Gender': forms.Select(
                choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                attrs={'class': 'custom-select'}
            ),
            'Health_Issues': forms.Textarea(attrs={'class': 'custom-textarea', 'rows': 3}),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'user', 'Profile_Picture', 'subject_specialization', 'years_of_experience', 'Age',
            'Next_Of_Kin', 'Phone_Number', 'State_Of_Origin', 'Local_Government', 'Country_Of_Origin',
            'Town_Of_Origin', 'Gender', 'Health_Issues', 'identification_type', 'identification_number'
        ]
        widgets = {
            'user': forms.Select(attrs={'class': 'custom-input'}),
            'Profile_Picture': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'subject_specialization': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Enter specialization'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'custom-input', 'min': 0}),
            'Age': forms.NumberInput(attrs={'class': 'custom-input', 'min': 18}),
            'Next_Of_Kin': forms.TextInput(attrs={'class': 'custom-input'}),
            'Phone_Number': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Enter phone number'}),
            'State_Of_Origin': forms.TextInput(attrs={'class': 'custom-input'}),
            'Local_Government': forms.TextInput(attrs={'class': 'custom-input'}),
            'Country_Of_Origin': forms.TextInput(attrs={'class': 'custom-input'}),
            'Town_Of_Origin': forms.TextInput(attrs={'class': 'custom-input'}),
            'Gender': forms.Select(
                choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                attrs={'class': 'custom-select'}
            ),
            'Health_Issues': forms.Textarea(attrs={'class': 'custom-textarea', 'rows': 3}),
            'identification_type': forms.Select(attrs={'class': 'custom-select'}),
            'identification_number': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Enter ID Number'}),
        }