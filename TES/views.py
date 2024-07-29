from django.shortcuts import render, redirect
from .models import Plants, Commission, Employer, Exam
from .forms import EmployerForm, CommissionForm, ExamForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def index(request):
    return render(request, 'TES/index.html')


def plants_view(request):
    plants = Plants.objects.all()
    context = {
        'plants': plants
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
