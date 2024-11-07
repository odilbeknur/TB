from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django_select2.forms import Select2MultipleWidget

STATUSES = (
        (u'pass', u'Прошел'),
        (u'fail', u'Не прошел'),
        (u'process', u'В процессе'),
    )


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_num', 'name', 'image','level', 'department', 'position', 'enter', 'pos_duration','gender', 'birth_date', 'region','plant']
        widgets = {
            'employee_num': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'level': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'department': forms.Select(attrs={
                'class': 'form-control'
            }),
            'position': forms.Select(attrs={
                'class': 'form-control'
            }),
            'enter': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'pos_duration': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control'
            }),
            'region': forms.Select(attrs={
                'class': 'form-control'
            }),
            'plant': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


class CommissionForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=Select2MultipleWidget(attrs={'class': 'form-control select2'}),  # Add 'form-control select2' classes
        required=False,
        label="Члены комиссии"
    )

    class Meta:
        model = Commission
        fields = ['name', 'leader', 'lvl', 'group', 'commission_type', 'image', 'members']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название комиссии'
            }),
            'leader': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'lvl': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите разряд'
            }),
            'group': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите группу'
            }),
            'commission_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }
            ),
        }


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['name','types','start','end','plant','commission']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'types': forms.Select(attrs={
                'class': 'form-control'
            }),
            'start': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }),
            'end': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }),
            'plant': forms.Select(attrs={
                'class': 'form-control'
            }),
            'commission': forms.Select(attrs={  
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


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    role = forms.Select(attrs={
        'class': 'form-control'
    })
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# class ScoreForm(forms.ModelForm):
#     class Meta:
#         model = Score
#         fields = ['name', 'score', 'exam', 'status']
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'form-control'
#             }),
#             'score': forms.NumberInput(attrs={
#                 'class': 'form-control'
#             }),
#             'exam': forms.Select(attrs={
#                 'class': 'form-control'
#             }),
#             'status': forms.Select(attrs={
#                 'class': 'form-control'
#             })
#         }

# class ScoreForm(forms.ModelForm):
#     class Meta:
#         model = Score
#         fields = ['name', 'score', 'status']
    
#     name = forms.ModelChoiceField(queryset=Employer.objects.all(), label='Student')
#     score = forms.FloatField(label='Score')
#     status = forms.ChoiceField(choices=STATUSES, label='Status')

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['name', 'score', 'status']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),  
            'score': forms.NumberInput(attrs={
                'class': 'form-control'
            }),  
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),  
        }


class SearchForm(forms.Form):
    query = forms.CharField()
