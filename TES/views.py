from django.contrib.auth import logout, login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Plants, Commission, Employer, Exam
from .forms import EmployerForm, CommissionForm, ExamForm, LoginForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def index(request):
    return render(request, 'TES/index.html')


def plants_view(request):
    plants = Plants.objects.all()
    employers = Employer.objects.all()
    plant_id = request.GET.get('plant')
    if plant_id:
        employers = Employer.objects.filter(plant=Plants.objects.get(pk=plant_id))
        print('Success')
    else:
        plant_id = 0
        print('Error')
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


def exam_view(request):
    exams = Exam.objects.all()
    context = {
        'exams': exams
    }
    return render(request, 'TES/index.html', context)


def exam_create(request):
    if request.method == 'POST':
        form = ExamForm(request.POST, request.FILES)
        if form.is_valid():
            exam = form.save()
            exam.save()
            return redirect('index')
    else:
        form = ExamForm()
        context = {
            'form': form,
            'title': 'Добавить экзамен'
        }
        return render(request, 'TES/index.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)

                return redirect('index')
            else:

                return redirect('index')


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

# поиск
# калакольчик
# описание
# аватарка
# учасники
# календарь
# профиль
# визуал
