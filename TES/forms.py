from django import forms
from .models import Employer, Commission, Exam, Score
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['name', 'level', 'position', 'pos_duration', 'enter', 'plant', 'commission', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'level': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'commission': forms.Select(attrs={
                'class': 'form-control'
            }),
            'pos_duration': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'enter': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'plant': forms.Select(attrs={
                'class': 'form-control'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['user_name', 'lvl', 'group', 'commission_type', 'image', 'description']
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'lvl': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'group': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'commission_type': forms.Select(attrs={
                'class': 'form-control'
            })
        }


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['type', 'date', 'plant']
        widgets = {
            'type': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control'
            }),
            'plant': forms.Select(attrs={
                'class': 'form-control'
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['name', 'score', 'exam']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'score': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'exam': forms.Select(attrs={
                'class': 'form-control'
            })
        }
