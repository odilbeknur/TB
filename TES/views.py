from django.shortcuts import render, redirect
from .models import Plants, Commission, Employer
from .forms import EmployerForm, CommissionForm
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
    print('1')
    if request.method == 'POST':
        print('2')
        form = CommissionForm(request.POST, request.FILES)
        if form.is_valid():
            print('3')
            commission = form.save()
            commission.save()
            return redirect('commission')
    else:
        print('4')
        form = CommissionForm()
        context = {
            'form': form,
            'title': 'Добавить Коммиссию'
        }
        print('5')
        return render(request, 'TES/commission_form.html', context)
