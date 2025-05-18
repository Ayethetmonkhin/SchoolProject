from django import forms
from .models import *

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['photo', 'name', 'fee','description']

class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['photo','name','course','description']

class  UpdateCourseFm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['photo','name','fee','description']
        wiidgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),
            'description': forms.Textarea(attrs={'class':'forms-control'})
        }