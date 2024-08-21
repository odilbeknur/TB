from django.contrib.auth import logout, login
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import EmployerForm, CommissionForm, ExamForm, LoginForm, ScoreForm, RegistrationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.core.paginator import Paginator

from django.http import JsonResponse 
from django.utils import timezone

def index(request):
    all_events = Exam.objects.all()
    total_employees = Employer.objects.count()
    passed_exams = Score.objects.filter(status='pass').count()
    in_progress_exams = Score.objects.filter(status=None).count()
    failed_exams = Score.objects.filter(status='fail').count()
    context = {
        'total_employees': total_employees,
        'passed_exams': passed_exams,
        'in_progress_exams': in_progress_exams,
        'failed_exams': failed_exams,
        "events":all_events
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

    paginator = Paginator(commissions, 8)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'commissions': page_obj
    }
    return render(request, 'TES/commission.html', context)


def employer_view(request):
    employers = Employer.objects.all()

    paginator = Paginator(employers, 8)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'employers': page_obj
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
    filter_name = request.GET.get('name')

    if filter_name:
        exams = exams.filter(type=filter_name)

    paginator = Paginator(exams, 8)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'exams': page_obj,
        'employers': Employer.objects.all(),
        'filter_name': filter_name
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
            'title': 'Добавить комиссию'
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

    paginator = Paginator(employers, 8)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'employers': page_obj,
    }
    return render(request, 'TES/plant_detail.html', context)


def commission_detail(request, pk):
    commission = get_object_or_404(Commission, id=pk)
    exam = get_object_or_404(Exam, id=pk)

    employers = Employer.objects.filter(exam=exam)
    files = Files.objects.filter(commission=commission)
    print(employers)
    context = {
        'employers': employers,
        'exam': exam,
        'commission': commission,
        'files': files
    }
    return render(request, 'TES/commission_detail.html', context)


def employer_detail(request, pk):
    employer = get_object_or_404(Employer, id=pk)
    commissions = Commission.objects.filter(employer=employer)
    exams = Exam.objects.filter(employer=employer)
    scores = Score.objects.filter(name=employer)

    paginator = Paginator(exams, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    context = {
        'commissions': commissions,
        'employer': employer,
        'exams': page_obj,
        'scores': scores
    }
    return render(request, 'TES/employer_detail.html', context)


def exam_detail(request, pk):
    exam = get_object_or_404(Exam, id=pk)
    employers = Employer.objects.all()
    scores = Score.objects.filter(exam_id=exam.id)

    paginator = Paginator(employers, 8)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    print(exam)
    context = {
        'exam': exam,
        'employers': page_obj,
        'scores': scores
    }

    return render(request, 'TES/exam_detail.html', context)



def all_events(request):
    all_events = Exam.objects.all()
    out = []
    now = timezone.now()  # Get current time using Django's timezone utility
    for event in all_events:
        status = "outdated" if event.end < now else "upcoming"  # Example status logic
        plant_name = event.plant.name if event.plant else "Unknown Plant"
        out.append({
            'title': event.type + " экзамен в " + plant_name,  # Include type and plant name in title
            'start': event.start.strftime("%Y-%m-%dT%H:%M:%S"),
            'end': event.end.strftime("%Y-%m-%dT%H:%M:%S"),
            'status': status,
        })
        
    return JsonResponse(out, safe=False)

 
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Exam(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)
 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Exam.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Exam.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)

def passed(request):
    passed_exams = Score.objects.filter(status='pass')
    context = {
        'passed_exams': passed_exams
    }
    print(passed_exams)
    return render(request, 'dashpass/passed.html', context)
def process(request):
    process_exams = Score.objects.filter(status=None)
    context = {
        'process_exams': process_exams
    }
    return render(request, 'dashpass/process.html', context)
def failed(request):
    failed_exams = Score.objects.filter(status='fail')
    context = {
        'failed_exams': failed_exams
    }
    return render(request, 'dashpass/failed.html', context)