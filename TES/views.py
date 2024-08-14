from django.contrib.auth import logout, login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Plants, Commission, Employer, Exam, User, Score, Files
from .forms import EmployerForm, CommissionForm, ExamForm, LoginForm, ScoreForm, RegistrationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages


def index(request):
    total_employees = Employer.objects.count()
    passed_exams = Score.objects.filter(status='pass').count()
    in_progress_exams = Score.objects.filter(status=None).count()
    failed_exams = Score.objects.filter(status='fail').count()
    print(passed_exams)
    context = {
        'total_employees': total_employees,
        'passed_exams': passed_exams,
        'in_progress_exams': in_progress_exams,
        'failed_exams': failed_exams
    }
    return render(request, 'TES/index.html', context)


def plants_view(request):
    plants = Plants.objects.all()
    employers = Employer.objects.all()
    plant_id = request.GET.get('plant')
    if plant_id:
        employers = Employer.objects.filter(plant=Plants.objects.get(pk=plant_id))
        print('Success')
    else:
        plant_id = 0
    context = {
        'plants': plants,
        'employers': employers,
        'plant_id': int(plant_id)
    }
    return render(request, 'TES/plants.html', context)


def commission_view(request):
    commissions = Commission.objects.all()
    context = {
        'commissions': commissions
    }
    return render(request, 'TES/commission.html', context)


def employer_view(request):
    employers = Employer.objects.all()
    context = {
        'employers': employers
    }
    return render(request, 'TES/employers.html', context)


def employer_create(request):
    if request.method == 'POST':
        form = EmployerForm(request.POST, request.FILES)
        if form.is_valid():
            employer = form.save()
            employer.save()
            return redirect('employer')
    else:
        form = EmployerForm()
        context = {
            'form': form,
            'title': 'Добавить сотрудника'
        }
        return render(request, 'TES/employer_form.html', context)


def exam_view(request):
    exams = Exam.objects.all()
    employers = Employer.objects.all()
    context = {
        'exams': exams,
        'employers': employers
    }
    return render(request, 'TES/exam.html', context)


def exam_create(request):
    if request.method == 'POST':
        form = ExamForm(request.POST, request.FILES)
        if form.is_valid():
            exam = form.save()
            exam.save()
            return redirect('exam')
    else:
        form = ExamForm()
        context = {
            'form': form,
            'title': 'Добавить экзамен'
        }
        return render(request, 'TES/exam_form.html', context)


def commission_create(request):
    if request.method == 'POST':
        form = CommissionForm(request.POST, request.FILES)
        if form.is_valid():
            commission = form.save()
            commission.save()
            return redirect('commission')
    else:
        form = CommissionForm()
        context = {
            'form': form,
            'title': 'Добавить Коммиссию'
        }
        return render(request, 'TES/commission_form.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print('USER: ', user)

            if user:
                login(request, user)
                return redirect('index')
            else:
                return redirect('index')
        else:
            print(form.errors.as_data())
            return redirect('index')
    else:
        form = LoginForm()

    context = {
        'form': form,
        'title': 'Авторизация'
    }
    return render(request, 'TES/user_form.html', context)


def user_create(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')
        else:
            return redirect('index')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
        'title': 'Создание пользователя'
    }
    return render(request, 'TES/user_form.html', context)


def user_logout(request):
    logout(request)

    return redirect('index')


def login_form(request):
    context = {
        'login_form': LoginForm(),
        'title': 'Вход в аккаунт'
    }
    return render(request, 'TES/auth.html', context)


class CommissionDetail(DetailView):
    model = Commission
    context_object_name = 'commission'
    template_name = 'TES/commission_detail.html'


class EmployerDetail(DetailView):
    model = Employer
    context_object_name = 'employer'
    template_name = 'TES/employer_detail.html'


class PlantDetail(DetailView):
    model = Plants
    context_object_name = 'plant'
    template_name = 'TES/plant_detail.html'


def plants_detail(request, pk):
    plant = get_object_or_404(Plants, id=pk)
    employers = Employer.objects.filter(plant_id=plant.id)
    context = {
        'employers': employers,
    }
    return render(request, 'TES/plant_detail.html', context)


def commission_detail(request, pk):
    commission = get_object_or_404(Commission, id=pk)
    employers = Employer.objects.filter(commission=commission)
    files = Files.objects.filter(commission=commission)
    context = {
        'employers': employers,
        'commission': commission,
        'files': files
    }
    return render(request, 'TES/commission_detail.html', context)


def employer_detail(request, pk):
    employer = get_object_or_404(Employer, id=pk)
    print('employer:    ', employer)
    commissions = Commission.objects.filter(employer=employer)
    print('commission.objects.filter(user_name=employer):         ', commissions)

    print("commissions.pk:    ", [i.pk for i in commissions])

    context = {
        'commissions': commissions,
        'employer': employer
    }
    print(commissions)
    return render(request, 'TES/employer_detail.html', context)


def exam_detail(request, pk):
    exam = get_object_or_404(Exam, id=pk)
    employers = Employer.objects.filter(exam_id=exam.id)
    scores = Score.objects.all()
    context = {
        'exam': exam,
        'employers': employers,
        'scores': scores
    }
    return render(request, 'TES/exam_detail.html', context)

# поиск
# календарь
# визуал
